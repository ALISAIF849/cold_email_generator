import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)
def generate_email(company, role, skills):
    prompt = f"""
You are a professional career assistant.

Write a short, polite, and professional cold email for a job application.

Company: {company}
Role: {role}
Candidate Skills: {skills}

The email should be confident, friendly, and concise.
"""

    response = llm.invoke(prompt)
    return response.content