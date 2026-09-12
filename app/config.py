import os


class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-secret"
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///../instance/combs.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
