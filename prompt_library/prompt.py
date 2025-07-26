def generate_profile_prompt(goal, activity_level, sleep_hours, stress_level):
    return (
        f"A user has the following health profile:\n"
        f"Goal: {goal or 'Not specified'}\n"
        f"Activity Level: {activity_level or 'Not specified'}\n"
        f"Average Sleep: {sleep_hours if sleep_hours is not None else 'Not specified'} hours\n"
        f"Stress Level: {stress_level or 'Not specified'}\n\n"
        "Generate actionable and personalized health advice based on this."
    )

def generate_direct_question_prompt(question):
    return (
        f"User asked: {question}\n"
        "Give a thoughtful and medically accurate answer."
    )
