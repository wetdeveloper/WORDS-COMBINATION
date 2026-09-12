from flask import Blueprint, request, jsonify

from app.services.security.analyzer import analyze


security_bp = Blueprint(
    "security",
    __name__,
    url_prefix="/api/security"
)


@security_bp.route("/analyze", methods=["POST"])
def security_analyze():

    data = request.json

    result = analyze(
        data["charset"],
        data["length"],
        data.get("speed", 1000)
    )

    return jsonify(result)
