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
st.title("Text For Tech Generator")
st.write("Generate code, write emails, or paraphrase text using AI.")

# User input
option = st.selectbox("Select Task", ["Generate Code", "Write an Email", "Paraphrase Text"])
user_input = st.text_area("Enter Your Requirement")

if option == "Generate Code":
    code_language = st.selectbox("Select Programming Language", ["Python", "Java","html", "C++", "JavaScript", "SQL", "SAS", "Other"])
    if st.button("Generate") and user_input:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
        full_prompt = (
            f"You are an expert programmer. Generate optimized and well-structured {code_language} code "
            f"based on the following requirement:\n\n{user_input}\n\nProvide the complete solution with comments where necessary."
        )
        response = llm.predict(full_prompt)
        st.write("### Generated Code:")
        st.code(response, language=code_language.lower() if code_language != "Other" else "plaintext")

elif option == "Write an Email":
    email_tone = st.selectbox("Select Tone", ["Formal", "Informal", "Persuasive", "Apologetic", "Thank You"])
    if st.button("Generate Email") and user_input:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
        full_prompt = (
            f"You are an expert email writer. Write a {email_tone.lower()} email based on the following input:\n\n{user_input}\n\nEnsure it is well-structured and effective."
        )
        response = llm.predict(full_prompt)
        st.write("### Generated Email:")
        st.text_area("Email Output", response, height=200)

elif option == "Paraphrase Text":
    if st.button("Paraphrase") and user_input:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=openai_api_key)
        full_prompt = (
            f"Rephrase the following text in a clear and professional manner:\n\n{user_input}"
        )
        response = llm.predict(full_prompt)
        st.write("### Paraphrased Text:")
        st.text_area("Output", response, height=200)

# Sidebar with instructions
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=150)

