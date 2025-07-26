from langchain_openai import ChatOpenAI
import os
from utils.config_loader import load_config

class ModelLoader:
    def load_llm(self):
        return ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))





class ModelLoader:
    def __init__(self):
        self.config = load_config()  # Load config.yaml once during initialization

    def load_llm(self):
        model_name = self.config["llm"]["model_name"]
        api_key = os.getenv("OPENAI_API_KEY")
        return ChatOpenAI(model=model_name, openai_api_key=api_key)
