"""
ml_service.py

Integration contract between the backend and the ML risk-scoring model.

Ownership: this module's real scoring logic (feature engineering, anomaly
detection, fraud detection, risk scoring, model training, model inference)
belongs to the ML teammate and is NOT implemented here. This file currently
defines ONLY the interface the backend calls against: an exception type
and a function signature.

Contract:
    Input:  a single project dict, in the exact JSON-safe shape already
            returned by services.data_service.get_project_by_id() —
            same keys, same None-for-missing convention, same date-as-
            ISO-string format. This module never touches pandas, the
            CSV, or data_service.py directly.
    Output: a JSON-serializable dict. The only field the backend relies
            on structurally is "project_id" (to match the response back
            to the request); all other fields are the ML side's to
            define (e.g. risk_score, risk_level, reasons, model_version).

Until the ML teammate replaces the body of score_project() with real
model inference, every call raises MLServiceError so the backend can
report "ML model not connected yet" distinctly from other failures.
"""
from typing import Any, Dict


class MLServiceError(Exception):
    """Raised when the ML scoring model is unavailable, not yet
    implemented, or fails to produce a score."""


def score_project(project: Dict[str, Any]) -> Dict[str, Any]:
    """
    Score a single project and return a risk result.

    Args:
        project: a project record dict, matching the shape returned by
            services.data_service.get_project_by_id().

    Returns:
        A JSON-serializable dict describing the project's risk, once
        implemented. Currently NOT IMPLEMENTED.

    Raises:
        MLServiceError: always, until the ML teammate implements real
            model inference in place of this stub. This is intentional
            and signals "ML model not connected yet" rather than a bug.
    """
    raise MLServiceError(
        "ML risk-scoring model is not connected yet. "
        "services/ml_service.py is currently a stub with no inference "
        "logic — this will be implemented separately."
    )