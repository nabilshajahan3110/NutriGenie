import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama3-8b-8192")

def get_nutrition_response(user_question, profile, chunks):
    context = "\n\n".join([chunk.page_content for chunk in chunks])
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful dietitian. Use the context and profile to answer."),
        ("human", "Profile:\n{profile}\n\nContext:\n{context}\n\nQuestion:\n{question}")
    ])
    prompt = prompt_template.format_messages(profile=profile, context=context, question=user_question)
    return llm.invoke(prompt).content