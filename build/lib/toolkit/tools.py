from langchain.tools import tool

@tool
def fitness_tool(activity_level: str, goal: str) -> str:
    """Gives fitness advice based on activity level and goal."""
    return f"For {activity_level} activity and your goal to {goal}, start with 30 min daily brisk walking."

@tool
def nutrition_tool(goal: str) -> str:
    """Recommends a diet based on fitness goal."""
    return f"For your goal to {goal}, focus on high-protein, low-carb meals and hydrate well."

@tool
def sleep_tool(sleep_hours: float) -> str:
    """Gives sleep improvement suggestions."""
    if sleep_hours < 6:
        return "Try to sleep at least 7-8 hours by creating a bedtime routine and avoiding screens before bed."
    else:
        return "You're getting good sleep! Maintain this habit."

@tool
def mental_health_tool(stress_level: str) -> str:
    """Gives mental wellness tips based on stress level."""
    return f"Since your stress is {stress_level}, practice meditation or journaling daily."
