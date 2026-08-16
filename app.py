import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Study Assistant")
st.write("Learn any topic with the help of AI.")

topic = st.text_input(
    "Enter a topic you want to learn:",
    placeholder="Example: Stack in Data Structures"
)

if st.button("Explain Topic"):
    if topic:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

        prompt = f"""
        You are an AI Study Assistant for college students.

        Explain the following topic clearly:
        {topic}

        Give the answer in this format:
        1. Simple Definition
        2. Detailed Explanation
        3. Real-life Example
        4. Important Points
        5. One Simple Example
        6. 5 Revision Questions
        """

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        st.markdown(response.text)
    else:
        st.warning("Please enter a topic first.")