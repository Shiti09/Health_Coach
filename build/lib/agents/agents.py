# File: graph_builder.py

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from langchain_core.messages import AIMessage, HumanMessage
from typing_extensions import Annotated, TypedDict

from utils.model_loaders import ModelLoader
from toolkit.health_tools import fitness_tool, nutrition_tool, sleep_tool, mental_health_tool  # your health tools

class State(TypedDict):
    messages: Annotated[list, add_messages]

class HealthCoachGraphBuilder:
    def __init__(self):
        self.model_loader = ModelLoader()
        self.llm = self.model_loader.load_llm()
        
        # Tools related to health advice
        self.tools = [
            fitness_tool,
            nutrition_tool,
            sleep_tool,
            mental_health_tool
        ]
        
        # Bind tools to LLM
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        self.graph = None

    def _chatbot_node(self, state: State):
        return {"messages": [self.llm_with_tools.invoke(state["messages"])]}

    def build(self):
        graph_builder = StateGraph(State)
        
        graph_builder.add_node("chatbot", self._chatbot_node)
        
        tool_node = ToolNode(tools=self.tools)
        graph_builder.add_node("tools", tool_node)
        
        graph_builder.add_conditional_edges("chatbot", tools_condition)
        graph_builder.add_edge("tools", "chatbot")
        graph_builder.add_edge(START, "chatbot")
        
        self.graph = graph_builder.compile()

    def get_graph(self):
        if self.graph is None:
            raise ValueError("Graph not built. Call build() first.")
        return self.graph
