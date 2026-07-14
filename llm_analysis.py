from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_answer(question, expected_answer, user_answer):
    """
    Compare user's answer with the expected answer
    and return similarity score.
    """
    expected_embedding = model.encode(expected_answer, convert_to_tensor=True)
    user_embedding = model.encode(user_answer, convert_to_tensor=True)
    similarity = util.cos_sim(
        expected_embedding,
        user_embedding
    ).item()
    percentage = round(similarity * 100, 2)
    if percentage >= 85:
        feedback = "Excellent Answer"
    elif percentage >= 70:
        feedback = "Good Answer"
    elif percentage >= 50:
        feedback = "Average Answer"
    else:
        feedback = "Needs Improvement"
    return {
        "score": percentage,
        "feedback": feedback
    }