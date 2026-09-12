from datetime import datetime



def generate_markdown_report(
    analysis,
    title="Security Analysis Report"
):

    report = f"""
# {title}

Generated:
{datetime.utcnow()}

---

## Input

Charset Size:
{analysis["charset_size"]}

Length:
{analysis["length"]}


## Search Space

Total Combinations:

{analysis["total_combinations"]}


## Risk Level

{analysis["risk"]}


## Estimated Time

Seconds:
{analysis["estimated_time"]["seconds"]}

Minutes:
{analysis["estimated_time"]["minutes"]}

Hours:
{analysis["estimated_time"]["hours"]}


## Recommendation

"""

    if analysis["risk"] in [
        "VERY_WEAK",
        "WEAK"
    ]:
        report += (
            "Increase password length "
            "and use more character diversity."
        )

    else:
        report += (
            "Current configuration "
            "has a larger search space."
        )


    return report
