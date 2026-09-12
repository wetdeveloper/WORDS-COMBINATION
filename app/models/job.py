from datetime import datetime

from app.extensions import db


class GenerationJob(db.Model):

    __tablename__ = "generation_jobs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    elements = db.Column(
        db.Text,
        nullable=False
    )

    length = db.Column(
        db.Integer,
        nullable=False
    )

    mode = db.Column(
        db.String(64),
        nullable=False
    )

    total = db.Column(
        db.BigInteger,
        nullable=False
    )

    status = db.Column(
        db.String(32),
        default="created"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


