import json

from app.extensions import db
from app.models.job import GenerationJob
from app.services.executor.executor import execute_job

from app.services.generator.counter import (
    permutation_repeat,
    permutation_no_repeat,
    combination_repeat,
    combination_no_repeat,
)


def calculate_total(size, length, mode):

    if mode == "permutation_repeat":
        return permutation_repeat(size, length)

    elif mode == "permutation_no_repeat":
        return permutation_no_repeat(size, length)

    elif mode == "combination_repeat":
        return combination_repeat(size, length)

    elif mode == "combination_no_repeat":
        return combination_no_repeat(size, length)

    else:
        raise ValueError("invalid mode")



def create_job(elements, length, mode):

    total = calculate_total(
        len(elements),
        length,
        mode
    )

    job = GenerationJob(
        elements=json.dumps(elements),
        length=length,
        mode=mode,
        total=total,
        status="created"
    )

    db.session.add(job)
    db.session.commit()

    execute_job(job)

    return job



def get_job(job_id):

    return GenerationJob.query.get(job_id)
