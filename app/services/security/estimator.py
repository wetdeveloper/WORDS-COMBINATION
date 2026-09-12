def estimate_time(
    combinations,
    speed
):

    if speed <= 0:
        raise ValueError(
            "speed must be positive"
        )

    seconds = combinations / speed

    return {
        "seconds": seconds,
        "minutes": seconds / 60,
        "hours": seconds / 3600,
        "days": seconds / 86400,
    }
