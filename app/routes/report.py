from flask import Blueprint, request, jsonify
from pathlib import Path

from app.services.security.analyzer import analyze
from app.services.security.reports.markdown import generate_markdown_report


report_bp = Blueprint(
    "report",
    __name__,
    url_prefix="/api/security"
)


@report_bp.route("/report", methods=["POST"])
def create_report():

    data = request.json

    result = analyze(
        data["charset"],
        data["length"],
        data.get("speed", 1000)
    )

    report = generate_markdown_report(result)

    path = Path(
        "reports/security_report.md"
    )

    path.write_text(report)

    return jsonify({
        "status": "created",
        "file": str(path),
        "risk": result["risk"]
    })

    return jsonify({
        "status": "created",
        "file": str(path),
        "risk": result["risk"]
    })
