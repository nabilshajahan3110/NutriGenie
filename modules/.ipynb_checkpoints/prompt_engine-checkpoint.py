from langchain_groq import ChatGroq
import os
import streamlit as st
from modules.rag_engine import load_docs, build_vector_store, get_relevant_chunks

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Lazy-loading: only build vectorstore once, and reuse it
@st.cache_resource(show_spinner=False)
def get_vectorstore():
    pdf_path = "data/diabetes_guidelines.pdf"
    docs = load_docs(pdf_path)
    return build_vector_store(docs)

def get_nutrition_response(query, profile):
    # Load lightweight LLM
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-8b-8192"
    )

    # Lazy load vectorstore
    vectorstore = get_vectorstore()

    # Retrieve context
    relevant_docs = get_relevant_chunks(vectorstore, query)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # Prompt engineering
    prompt = f"""
You are NutriGenie, a medically cautious nutrition assistant.

User profile:
- Age: {profile['age']}
- Weight: {profile['weight']} kg
- Goal: {profile['goal']}
- Allergies: {profile['allergies']}

Context from nutrition guidelines:
{context}

Question: {query}

Answer clearly and cite the PDF when relevant. Keep it concise and beginner-friendly.
"""

    return llm.invoke(prompt).content