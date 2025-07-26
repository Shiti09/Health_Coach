from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class ModelLoader:
    def load_llm(self):
        return ChatOpenAI(model="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))