def calculate_risk(
    total_combinations
):

    if total_combinations < 100000:
        return "VERY_WEAK"

    if total_combinations < 10000000:
        return "WEAK"

    if total_combinations < 10000000000:
        return "MEDIUM"

    if total_combinations < 100000000000000:
        return "STRONG"

    return "VERY_STRONG"
