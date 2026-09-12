from app.services.security.estimator import estimate_time
from app.services.security.risk import calculate_risk



def calculate_space(
    charset_size,
    length
):

    return charset_size ** length



def analyze(
    charset,
    length,
    speed=1000
):

    total = calculate_space(
        len(charset),
        length
    )

    return {
        "charset_size": len(charset),
        "length": length,
        "total_combinations": total,
        "risk": calculate_risk(total),
        "estimated_time": estimate_time(
            total,
            speed
        )
    }
