from flask import Blueprint, request, jsonify

from app.services.jobs.job_manager import (
    create_job,
    get_job,
)


api_bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


@api_bp.route("/jobs", methods=["POST"])
def create():

    data = request.json

    job = create_job(
        data["elements"],
        data["length"],
        data["mode"]
    )

    return jsonify({
        "id": job.id,
        "total": job.total,
        "status": job.status
    })



@api_bp.route("/jobs/<int:job_id>")
def detail(job_id):

    job = get_job(job_id)

    if not job:
        return {
            "error": "not found"
        }, 404


    return jsonify({
        "id": job.id,
        "elements": job.elements,
        "length": job.length,
        "mode": job.mode,
        "total": job.total,
        "status": job.status
    })
