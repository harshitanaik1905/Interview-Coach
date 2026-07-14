def generate_feedback(score):
    """
    Generate interview feedback based on the candidate's score.
    """
    if score >= 90:
        return {
            "performance": "Excellent",
            "strengths": [
                "Strong technical knowledge",
                "Excellent communication",
                "Clear explanation"
            ],
            "improvements": [
                "Continue practicing advanced interview questions."
            ]
        }
    elif score >= 75:
        return {
            "performance": "Good",
            "strengths": [
                "Good understanding of concepts",
                "Answered most questions correctly"
            ],
            "improvements": [
                "Provide more real-world examples.",
                "Improve confidence while answering."
            ]
        }
    elif score >= 50:
        return {
            "performance": "Average",
            "strengths": [
                "Basic understanding of concepts"
            ],
            "improvements": [
                "Revise technical fundamentals.",
                "Improve communication skills.",
                "Practice mock interviews regularly."
            ]
        }
    else:
        return {
            "performance": "Needs Improvement",
            "strengths": [
                "Shows willingness to learn."
            ],
            "improvements": [
                "Strengthen technical knowledge.",
                "Practice interview questions daily.",
                "Improve communication and confidence."
            ]
        }