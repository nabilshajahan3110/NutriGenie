# 🥗 NutriGenie – Your AI Nutrition Assistant

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge&logo=streamlit&labelColor=black)](https://nutrigeniegit-we86aqjmtg977birtugfl6.streamlit.app/)

NutriGenie is your personalized AI-powered nutrition assistant. It helps users — including diabetics, gym-goers, vegetarians, and those with dietary restrictions — make informed dietary decisions, grounded in real medical guidelines.

---

## ⚙️ Features

✅ **Personalized Profile Input**  
Set your age, weight, health goals, and allergies — and let NutriGenie tailor its recommendations accordingly.

✅ **Natural Language Nutrition Q&A**  
Ask questions like:
- “Can I eat jackfruit if I'm diabetic?”
- “Is tofu better than paneer for weight loss?”

✅ **Medical PDF Integration (RAG)**  
Answers are grounded in real **diabetes guidelines** using LangChain’s Retrieval-Augmented Generation (RAG).

✅ **Cited Sources**  
Every answer is backed by page-level chunks from the reference document.

✅ **Lightweight Deployment**  
Optimized for deployment on [Streamlit Community Cloud](https://streamlit.io/cloud).

---

## 🚀 Live Demo

Try NutriGenie in your browser (no installation needed):  
🔗 **[Launch App](https://nutrigeniegit-we86aqjmtg977birtugfl6.streamlit.app/)** 
---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **LLM**: Groq API (via Mixtral / LLaMA3 models)
- **RAG**: LangChain + FAISS + HuggingFace Embeddings
- **PDF Parsing**: PyPDFLoader
- **Backend**: Python 3.10+
- **Deployment**: Streamlit Cloud

---

## 🗂️ Project Structure
