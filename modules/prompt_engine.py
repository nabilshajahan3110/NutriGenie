from langchain_groq import ChatGroq
import os
import streamlit as st
from modules.rag_engine import load_docs, build_vector_store, get_relevant_chunks

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

# Load PDF documents
pdf_path = "data/diabetes_guidelines.pdf"
docs = load_docs(pdf_path)
vectorstore = build_vector_store(docs)

def get_nutrition_response(query, profile):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-70b-8192"  # or "gemma-7b-it"
    )

    # Retrieve chunks
    relevant_docs = get_relevant_chunks(vectorstore, query)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

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