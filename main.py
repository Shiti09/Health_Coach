from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utils.model_loaders import ModelLoader
from toolkit.health_tools import fitness_tool, nutrition_tool, sleep_tool, mental_health_tool
from prompt_library.prompt import generate_profile_prompt, generate_direct_question_prompt

app = FastAPI()
llm = ModelLoader().load_llm()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HealthQuery(BaseModel):
    goal: str = None
    activity_level: str = None
    sleep_hours: float = None
    stress_level: str = None
    question: str = None

@app.post("/query")
def get_health_advice(data: HealthQuery):
    if data.question:
        # Direct question
        prompt = generate_direct_question_prompt(data.question)
        response = llm.invoke(prompt)
        return {"answer": response.content}
    else:
        # Use profile-based advice
        prompt = generate_profile_prompt(
                goal=data.goal,
                activity_level=data.activity_level,
                sleep_hours=data.sleep_hours,
                stress_level=data.stress_level
            )
        response = llm.invoke(prompt)
        return {"advice": response.content}