from datetime import date
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from services.data_service import (
    DataLoadError,
    get_dashboard_summary,
    get_monthly_analytics,
    get_project_by_id,
    get_project_count,
    get_projects,
    get_vendor_analytics,
)
from services.ml_service import MLServiceError, score_project

app = FastAPI(title="MPLADGuard AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "MPLADGuard AI Backend is running",
        "system": "MPLADGuard-AI",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


# Kept for backward compatibility with the original health route.
@app.get("/api/health")
def api_health():
    return {"status": "online", "system": "MPLADGuard-AI"}


@app.get("/api/projects")
def list_projects(
    limit: int = Query(default=None, ge=1),
    offset: int = Query(default=0, ge=0),
    constituency: str = Query(default=None),
    vendor_id: str = Query(default=None),
    work_description: str = Query(default=None),
    is_fraud_label: int = Query(default=None, ge=0, le=1),
    sanction_date_from: date = Query(default=None),
    sanction_date_to: date = Query(default=None),
    min_sanctioned_amount: float = Query(default=None),
    max_sanctioned_amount: float = Query(default=None),
):
    """Return project records loaded from the CSV dataset.

    Optional filters, all combined with AND, applied before pagination:
    constituency, vendor_id, work_description (exact match),
    is_fraud_label (0 or 1), sanction_date_from/sanction_date_to
    (inclusive date range), min_sanctioned_amount/max_sanctioned_amount
    (inclusive amount range).
    """
    try:
        return get_projects(
            limit=limit,
            offset=offset,
            constituency=constituency,
            vendor_id=vendor_id,
            work_description=work_description,
            is_fraud_label=is_fraud_label,
            sanction_date_from=sanction_date_from,
            sanction_date_to=sanction_date_to,
            min_sanctioned_amount=min_sanctioned_amount,
            max_sanctioned_amount=max_sanctioned_amount,
        )
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/projects/count")
def projects_count():
    """Return the total number of project records in the dataset."""
    try:
        return {"count": get_project_count()}
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/dashboard")
def dashboard():
    """Return aggregate dashboard summary statistics for the dataset."""
    try:
        return get_dashboard_summary()
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/analytics/monthly")
def analytics_monthly():
    """Return project counts and amounts aggregated by sanction_date month."""
    try:
        return get_monthly_analytics()
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/analytics/vendors")
def analytics_vendors():
    """Return project counts and amounts aggregated by vendor_id."""
    try:
        return get_vendor_analytics()
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/api/risk/{project_id}")
def get_project_risk(project_id: str):
    """Return an ML-based risk score for a single project.

    NOTE: the ML model is not connected yet — see services/ml_service.py.
    This endpoint currently returns HTTP 503 for every existing project
    until the ML teammate implements real scoring in that module.
    """
    try:
        project = get_project_by_id(project_id)
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    if project is None:
        raise HTTPException(
            status_code=404, detail=f"Project '{project_id}' not found"
        )
    try:
        return score_project(project)
    except MLServiceError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc


# NOTE: this route must stay registered AFTER /api/projects/count above,
# so a request to /api/projects/count is matched by the literal route
# rather than being captured here with project_id="count".
@app.get("/api/projects/{project_id}")
def get_project(project_id: str):
    """Return a single project record by its project_id."""
    try:
        project = get_project_by_id(project_id)
    except DataLoadError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    if project is None:
        raise HTTPException(
            status_code=404, detail=f"Project '{project_id}' not found"
        )
    return project