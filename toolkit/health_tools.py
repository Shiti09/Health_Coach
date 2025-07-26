
from langchain_core.tools import tool
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# FITNESS TOOL
class FitnessInput(BaseModel):
    activity_level: str = Field(..., description="Your weekly activity level, e.g., 'none', 'moderate', 'active'")
    goal: str = Field(..., description="Your health goal, e.g., 'lose weight', 'build muscle'")

@tool(args_schema=FitnessInput, description="Provide 2–3 fitness exercise suggestions based on activity level and goal.")
def fitness_tool(activity_level: str, goal: str) -> str:
    prompt = (
        f"Suggest 2 to 3 personalized fitness activities for someone with a {activity_level} activity level "
        f"who wants to {goal}. Present the suggestions as a numbered list."
    )
    return llm.invoke(prompt).content


# NUTRITION TOOL
class NutritionInput(BaseModel):
    goal: str = Field(..., description="Your health goal, e.g., 'lose weight', 'gain muscle'")

@tool(args_schema=NutritionInput, description="Provide 2–3 nutrition tips based on goal.")
def nutrition_tool(goal: str) -> str:
    prompt = (
        f"Suggest 2 to 3 practical nutrition or meal tips for someone whose goal is to {goal}. "
        f"Present the suggestions as a numbered list."
    )
    return llm.invoke(prompt).content


# SLEEP TOOL
class SleepInput(BaseModel):
    sleep_hours: float = Field(..., description="Average hours of sleep you get per night")

@tool(args_schema=SleepInput, description="Provide 2–3 suggestions to improve sleep based on sleep hours.")
def sleep_tool(sleep_hours: float) -> str:
    prompt = (
        f"A person sleeps around {sleep_hours} hours per night. Suggest 2 to 3 personalized tips to improve their sleep. "
        f"Present the suggestions as a numbered list."
    )
    return llm.invoke(prompt).content


# MENTAL HEALTH TOOL
class MentalHealthInput(BaseModel):
    stress_level: str = Field(..., description="Your current stress level, e.g., 'low', 'moderate', 'high'")

@tool(args_schema=MentalHealthInput, description="Provide 2–3 mental wellness tips based on stress level.")
def mental_health_tool(stress_level: str) -> str:
    prompt = (
        f"A person has a {stress_level} stress level. Suggest 2 to 3 mental wellness activities or habits they can adopt. "
        f"Present the suggestions as a numbered list."
    )
    return llm.invoke(prompt).content


