🧠 Agentic AI Health Coach – Multi-Agent System for Holistic Wellbeing
Overview:

This project showcases a multi-agent AI system designed to function as a personalized health coach, offering context-aware, evidence-based advice in four core domains of wellbeing:
🔹 Nutrition | 🔹 Exercise | 🔹 Sleep | 🔹 Stress Management

Each domain is handled by a dedicated agent, collectively contributing to a unified, human-like conversation that mimics real health coaching. The system is modular, scalable, and demonstrates the potential of LLM-powered agentic workflows in preventive healthcare.

💡 Key Features
🧩 Multi-agent architecture using autonomous, goal-driven agents for each health pillar

🧠 LLM-based reasoning with domain-specific prompt tuning and memory

🔄 Context sharing among agents for coherent, cross-domain recommendations

📈 Dynamic profiling based on user input, enabling personalization

🗣️ Conversational interface that mimics a real health coach

⚙️ Designed for integration into apps, chatbots, or wearable health ecosystems

🎯 Use Case
Imagine a user reporting poor sleep and irregular meals. The Sleep Agent will assess patterns, while the Nutrition Agent might identify late-night eating as a trigger. The Stress Agent can suggest relaxation routines, and the Exercise Agent will recalibrate activity to support better sleep—all working in concert.

This is not a chatbot—it’s a distributed, intelligent coaching system built on the principles of agentic AI and behavioral science.

🛠 Tech Stack
Python for orchestration

LangChain Multi-Agent Framework

OpenAI GPT-4 

Frontend: Streamlit 




command
uvicorn main:app --reload
streamlit run streamlit_ui.py
