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

# Streamlit UI
st.title("AI Code Generator")
st.write("Generate any type of code using AI based on your prompt.")

# User input
user_prompt = st.text_area("Enter Your Code Requirement")
code_language = st.selectbox("Select Programming Language", ["Python", "Java", "C++","html", "JavaScript", "SQL", "SAS", "Other"])

if st.button("Generate Code") and user_prompt:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
    
    full_prompt = (
        f"You are an expert programmer. Generate optimized and well-structured {code_language} code "
        f"based on the following requirement:\n\n{user_prompt}\n\nProvide the complete solution with comments where necessary."
    )
    
    response = llm.predict(full_prompt)
    
    st.write("### Generated Code:")
    st.code(response, language=code_language.lower() if code_language != "Other" else "plaintext")

# Sidebar with instructions
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=150)
