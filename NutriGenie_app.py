import streamlit as st
from modules.prompt_engine import get_nutrition_response
from modules.rag_engine import load_docs, build_vector_store, get_relevant_chunks

st.set_page_config(page_title="NutriGenie – Your AI Nutrition Assistant", layout="wide")

st.title("🥗 NutriGenie – Your AI Nutrition Assistant")

# Collect user input for personalization
with st.sidebar:
    st.header("🧑‍⚕️ Your Profile")
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    weight = st.number_input("Weight (kg)", min_value=1, max_value=200, value=70)
    health_goals = st.text_area("Health Goals", "Maintain weight, control sugar")
    allergies = st.text_input("Allergies (comma separated)", "gluten, dairy")
    profile = f"Age: {age}, Weight: {weight}, Goals: {health_goals}, Allergies: {allergies}"

    st.markdown("---")
    st.markdown("🔍 Based on medical guidelines")

# Build vectorstore at runtime (limited to 3 pages)
with st.spinner("🔄 Loading knowledge base..."):
    docs = load_docs("data/diabetes_guidelines.pdf")
    vectorstore = build_vector_store(docs)

# User query input
st.subheader("💬 Ask a nutrition question")
user_query = st.text_input("e.g., Is tofu good for diabetics?", key="query")

if user_query:
    with st.spinner("🔎 Thinking..."):
        relevant_chunks = get_relevant_chunks(vectorstore, user_query)
        response = get_nutrition_response(user_query, profile, relevant_chunks)
        st.success("Answer:")
        st.write(response)

    with st.expander("📚 Sources"):
        for i, chunk in enumerate(relevant_chunks, 1):
            st.markdown(f"**{i}.** {chunk.page_content.strip()[:300]}...")