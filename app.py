import streamlit as st
from langchain.chat_models import ChatOpenAI
import os

# Load OpenAI API key
try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

# Verify the API key is loaded
if not openai_api_key:
    st.error("OpenAI API key not found! Please set it in your Streamlit secrets or .env file.")
    st.stop()

# Custom CSS for better UI
def load_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextArea>label, .stSelectbox>label {
            font-weight: bold;
            color: #2e3a59;
        }
        .stCode {
            border-radius: 10px;
            background-color: #1e1e1e;
            color: #dcdcdc;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Load custom styles
load_custom_css()

# Streamlit UI
st.markdown("""
    <h1 style='text-align: center; color: #2e3a59;'>🚀 Text For Tech Generator</h1>
    <p style='text-align: center; font-size: 18px; color: #666;'>Generate code, write emails, or paraphrase text with AI.</p>
    """, unsafe_allow_html=True)

# User input
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=120)
st.sidebar.title("🔹 Instructions")
st.sidebar.write("1. Choose a task.")
st.sidebar.write("2. Enter your input.")
st.sidebar.write("3. Click the button to generate output.")

option = st.selectbox("🔍 Select Task", ["Generate Code", "Write an Email", "Paraphrase Text"], index=0)
user_input = st.text_area("✍️ Enter Your Requirement")

if option == "Generate Code":
    code_language = st.selectbox("💻 Select Programming Language", ["Python", "Java", "HTML", "C++", "JavaScript", "SQL", "SAS", "Other"])
    if st.button("🚀 Generate Code") and user_input:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
        full_prompt = (
            f"You are an expert programmer. Generate optimized and well-structured {code_language} code "
            f"based on the following requirement:\n\n{user_input}\n\nProvide the complete solution with comments where necessary."
        )
        response = llm.predict(full_prompt)
        st.subheader("📝 Generated Code:")
        st.code(response, language=code_language.lower() if code_language != "Other" else "plaintext")

elif option == "Write an Email":
    email_tone = st.selectbox("✉️ Select Tone", ["Formal", "Informal", "Persuasive", "Apologetic", "Thank You"])
    if st.button("📩 Generate Email") and user_input:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
        full_prompt = (
            f"You are an expert email writer. Write a {email_tone.lower()} email based on the following input:\n\n{user_input}\n\nEnsure it is well-structured and effective."
        )
        response = llm.predict(full_prompt)
        st.subheader("📧 Generated Email:")
        st.text_area("Email Output", response, height=200)

elif option == "Paraphrase Text":
    if st.button("🔄 Paraphrase") and user_input:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
        full_prompt = (
            f"Rephrase the following text in a clear and professional manner:\n\n{user_input}"
        )
        response = llm.predict(full_prompt)
        st.subheader("🔁 Paraphrased Text:")
        st.text_area("Output", response, height=200)

st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 14px; color: #777;'>
    Created with using Streamlit & OpenAI | <a href='https://www.openai.com' target='_blank'>Visit OpenAI</a>
    </p>
    """, unsafe_allow_html=True)
