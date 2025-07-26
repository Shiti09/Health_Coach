import streamlit as st
import requests
import sys
from exception.exceptions import HealthcoachException

BASE_URL = "http://localhost:8000"  # Backend endpoint

st.set_page_config(
    page_title="🧠 AI Health Coach",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🧠 Personalized Health Coach")
st.markdown("Get **fitness, nutrition, sleep, and mental wellness** advice tailored to your lifestyle.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for health inputs
with st.sidebar:
    st.header("📝 Health Profile")

    goal = st.selectbox("🎯 Health Goal", ["Lose weight", "Gain muscle", "Improve sleep", "Reduce stress"])
    activity_level = st.selectbox("🏃 Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    sleep_hours = st.slider("🛌 Average Sleep (hours)", min_value=0.0, max_value=12.0, value=6.0, step=0.5)
    stress_level = st.selectbox("😰 Stress Level", ["Low", "Moderate", "High"])

    if st.button("🧠 Get My Health Tips"):
        try:
            payload = {
                "goal": goal.lower(),
                "activity_level": activity_level.lower(),
                "sleep_hours": sleep_hours,
                "stress_level": stress_level.lower()
            }

            with st.spinner("Processing your inputs..."):
                response = requests.post(f"{BASE_URL}/query", json=payload)

            if response.status_code == 200:
                advice = response.json().get("advice", "No advice returned.")
                st.session_state.messages.append({"role": "bot", "content": advice})
                st.success("✅ Advice generated successfully!")
            else:
                st.error("❌ Failed to fetch advice: " + response.text)

        except Exception as e:
            raise HealthcoachException(e, sys)

# Display conversation history
st.header("💬 AI Health Coach Suggestions")
for chat in st.session_state.messages:
    st.markdown(f"**🤖 Coach:** {chat['content']}")

# Optional direct message box
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask the coach directly (optional)", placeholder="e.g. Can I skip breakfast?")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Bot is thinking..."):
            response = requests.post(f"{BASE_URL}/query", json={"question": user_input})

        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            st.session_state.messages.append({"role": "bot", "content": answer})
            st.rerun()
        else:
            st.error("❌ Bot failed to respond: " + response.text)

    except Exception as e:
        raise HealthcoachException(e, sys)

# Footer
st.markdown("---")
st.markdown(
    "<center><small>SHITHIL's Health Coach | Powered by AI</small></center>",
    unsafe_allow_html=True
)


