def calculate_score(ai_score):
    """
    Calculate interview scores.
    """
    technical = round(ai_score)
    communication = min(100, technical + 5)
    confidence = min(100, technical + 3)
    grammar = min(100, technical + 4)
    overall = round(
        (
            technical +
            communication +
            confidence +
            grammar
        ) / 4,
        2
    )
    return {
        "Technical": technical,
        "Communication": communication,
        "Confidence": confidence,
        "Grammar": grammar,
        "Overall": overall
    }