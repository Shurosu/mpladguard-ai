"""
data_service.py
Loads, validates, and parses the MPLADS project dataset from CSV.
Data loading / validation / basic type-parsing only — no anomaly
detection, ML, risk scoring, or database functionality here.
"""
from pathlib import Path
from datetime import date
from typing import Any, Dict, List, Optional
import pandas as pd

# ---------------------------------------------------------------------------
# Dataset path
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
CSV_PATH = DATA_DIR / "synthetic_sakshi_data.csv"

# ---------------------------------------------------------------------------
# Schema — matches the actual CSV
# ---------------------------------------------------------------------------
EXPECTED_COLUMNS = [
    "project_id",
    "constituency",
    "work_description",
    "vendor_id",
    "vendor_bank_acc",
    "vendor_ip_address",
    "sanctioned_amount_inr",
    "invoiced_amount_inr",
    "latitude",
    "longitude",
    "sanction_date",
    "is_fraud_label",
    "anomaly_reason",
]

NUMERIC_COLUMNS = [
    "sanctioned_amount_inr",
    "invoiced_amount_inr",
    "latitude",
    "longitude",
    "is_fraud_label",
]

DATE_COLUMNS = [
    "sanction_date",
]

# Module-level cache so the CSV is parsed only once per process.
_projects_df: Optional[pd.DataFrame] = None


class DataLoadError(Exception):
    """Raised when the dataset cannot be found, read, or validated."""


def _validate_columns(df: pd.DataFrame) -> None:
    """Validate that all expected columns exist in the dataset."""
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise DataLoadError(
            f"Dataset is missing expected column(s): {missing}. "
            f"Found columns: {list(df.columns)}"
        )


def load_projects(force_reload: bool = False) -> pd.DataFrame:
    """
    Load the MPLADS project CSV into a pandas DataFrame,
    validate its columns, and parse numeric/date fields.
    Cached after the first successful load.
    Pass force_reload=True to re-read the file from disk.
    """
    global _projects_df
    if _projects_df is not None and not force_reload:
        return _projects_df
    if not CSV_PATH.exists():
        raise DataLoadError(
            f"Dataset file not found at: {CSV_PATH}"
        )
    try:
        df = pd.read_csv(CSV_PATH)
    except Exception as exc:
        raise DataLoadError(
            f"Failed to read dataset CSV: {exc}"
        ) from exc
    _validate_columns(df)
    # Convert numeric fields.
    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # Convert date fields.
    for col in DATE_COLUMNS:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    _projects_df = df
    return _projects_df


def get_projects(
    limit: Optional[int] = None,
    offset: int = 0,
    constituency: Optional[str] = None,
    vendor_id: Optional[str] = None,
    work_description: Optional[str] = None,
    is_fraud_label: Optional[int] = None,
    sanction_date_from: Optional[date] = None,
    sanction_date_to: Optional[date] = None,
    min_sanctioned_amount: Optional[float] = None,
    max_sanctioned_amount: Optional[float] = None,
) -> List[Dict[str, Any]]:
    """
    Return project records as a list of JSON-serializable dictionaries.

    Optional filters (all applied before pagination, combined with AND):
        constituency:          exact match
        vendor_id:             exact match
        work_description:      exact match
        is_fraud_label:        exact match (0 or 1)
        sanction_date_from:    sanction_date >= this date
        sanction_date_to:      sanction_date <= this date
        min_sanctioned_amount: sanctioned_amount_inr >= this value
        max_sanctioned_amount: sanctioned_amount_inr <= this value

    Rows with a missing/invalid sanction_date (NaT) never match a date
    range filter, since it's unknown whether they fall within it.

    limit/offset are applied AFTER all filtering, so they paginate over
    the filtered result set, not the full dataset.
    """
    df = load_projects()

    if constituency is not None:
        df = df[df["constituency"] == constituency]
    if vendor_id is not None:
        df = df[df["vendor_id"] == vendor_id]
    if work_description is not None:
        df = df[df["work_description"] == work_description]
    if is_fraud_label is not None:
        df = df[df["is_fraud_label"] == is_fraud_label]
    if sanction_date_from is not None:
        df = df[df["sanction_date"] >= pd.Timestamp(sanction_date_from)]
    if sanction_date_to is not None:
        df = df[df["sanction_date"] <= pd.Timestamp(sanction_date_to)]
    if min_sanctioned_amount is not None:
        df = df[df["sanctioned_amount_inr"] >= min_sanctioned_amount]
    if max_sanctioned_amount is not None:
        df = df[df["sanctioned_amount_inr"] <= max_sanctioned_amount]

    if offset:
        df = df.iloc[offset:]
    if limit is not None:
        df = df.iloc[:limit]

    return _df_to_records(df)


def get_project_count() -> int:
    """Return the total number of project records."""
    df = load_projects()
    return int(len(df))


def get_project_by_id(project_id: str) -> Optional[Dict[str, Any]]:
    """
    Return a single project record matching the given project_id, or
    None if no such project exists in the dataset.
    """
    df = load_projects()
    match = df[df["project_id"] == project_id]
    if match.empty:
        return None
    return _df_to_records(match)[0]


def get_dashboard_summary() -> Dict[str, Any]:
    """
    Return aggregate dashboard statistics computed over the full cached
    dataset: total/fraud/clean project counts, total sanctioned and
    invoiced amounts, and the top 5 constituencies by project count.

    Pure aggregation over load_projects() — no ML, no anomaly scoring,
    no filtering of the underlying dataset.
    """
    df = load_projects()

    total_projects = int(len(df))
    fraud_projects = int((df["is_fraud_label"] == 1).sum())
    clean_projects = total_projects - fraud_projects

    # .sum() skips NaN by default, so missing amounts don't break the total.
    total_sanctioned_amount = float(df["sanctioned_amount_inr"].sum())
    total_invoiced_amount = float(df["invoiced_amount_inr"].sum())

    top_constituencies = [
        {"constituency": name, "project_count": int(count)}
        for name, count in df["constituency"].value_counts().head(5).items()
    ]

    return {
        "total_projects": total_projects,
        "fraud_projects": fraud_projects,
        "clean_projects": clean_projects,
        "total_sanctioned_amount": total_sanctioned_amount,
        "total_invoiced_amount": total_invoiced_amount,
        "top_constituencies": top_constituencies,
    }


def get_vendor_analytics() -> List[Dict[str, Any]]:
    """
    Aggregate the complete dataset by vendor_id, returning one summary
    record per vendor: project_count, fraud_projects, clean_projects,
    total_sanctioned_amount_inr, total_invoiced_amount_inr, and
    constituencies_count (number of distinct constituencies that vendor
    has worked in).

    Sorted by project_count descending.

    Pure aggregation over load_projects() — no ML, no anomaly scoring,
    no filtering of the underlying dataset.
    """
    df = load_projects()

    vendor_records = []
    for vendor_id, group in df.groupby("vendor_id"):
        project_count = int(len(group))
        fraud_projects = int((group["is_fraud_label"] == 1).sum())
        clean_projects = project_count - fraud_projects

        vendor_records.append({
            "vendor_id": vendor_id,
            "project_count": project_count,
            "fraud_projects": fraud_projects,
            "clean_projects": clean_projects,
            "total_sanctioned_amount_inr": float(group["sanctioned_amount_inr"].sum()),
            "total_invoiced_amount_inr": float(group["invoiced_amount_inr"].sum()),
            "constituencies_count": int(group["constituency"].nunique()),
        })

    vendor_records.sort(key=lambda r: r["project_count"], reverse=True)
    return vendor_records


def get_monthly_analytics() -> List[Dict[str, Any]]:
    """
    Aggregate projects by sanction_date month (YYYY-MM), returning one
    summary record per month: project_count, fraud_projects,
    clean_projects, sanctioned_amount_inr, invoiced_amount_inr.

    Rows with a missing/invalid sanction_date (parsed as NaT by
    load_projects()) are excluded from the aggregation rather than
    causing an error, since they cannot be assigned to a month.

    Pure aggregation over load_projects() — no ML, no anomaly scoring,
    no filtering of the underlying dataset.
    """
    df = load_projects()

    valid = df[df["sanction_date"].notna()].copy()
    valid["month"] = valid["sanction_date"].dt.strftime("%Y-%m")

    monthly_records = []
    # sort=True orders months chronologically, since "YYYY-MM" sorts
    # the same alphabetically as it does chronologically.
    for month, group in valid.groupby("month", sort=True):
        project_count = int(len(group))
        fraud_projects = int((group["is_fraud_label"] == 1).sum())
        clean_projects = project_count - fraud_projects

        monthly_records.append({
            "month": month,
            "project_count": project_count,
            "fraud_projects": fraud_projects,
            "clean_projects": clean_projects,
            "sanctioned_amount_inr": float(group["sanctioned_amount_inr"].sum()),
            "invoiced_amount_inr": float(group["invoiced_amount_inr"].sum()),
        })

    return monthly_records


def _df_to_records(
    df: pd.DataFrame
) -> List[Dict[str, Any]]:
    """
    Convert a DataFrame to JSON-safe dictionaries.
    Dates become ISO strings.
    NaN/NaT values become None.
    """
    out = df.copy()
    # Convert dates to YYYY-MM-DD strings.
    for col in DATE_COLUMNS:
        formatted = out[col].dt.strftime("%Y-%m-%d")
        out[col] = (
            formatted
            .astype(object)
            .where(formatted.notna(), None)
        )
    # Convert NaN numeric values to None.
    for col in NUMERIC_COLUMNS:
        out[col] = (
            out[col]
            .astype(object)
            .where(out[col].notna(), None)
        )
    # Convert remaining NaN values, such as anomaly_reason,
    # into None for JSON serialization.
    out = out.astype(object).where(pd.notna(out), None)
    return out.to_dict(orient="records")