from app.extensions import db

from app.services.generator.generator import generate
from app.services.generator.modes import GenerationMode


def execute_job(job):

    job.status = "running"
    db.session.commit()


    generator = generate(
        eval(job.elements),
        job.length,
        GenerationMode(job.mode)
    )


    count = 0

    for item in generator:

        count += 1

        if count >= 100:
            break


    job.status = "completed"

    db.session.commit()


    return count
