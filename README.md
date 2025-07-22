# 🥗 NutriGenie – Your AI-Powered Nutrition Assistant

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-green?style=for-the-badge)](https://nutrigenie.streamlit.app)

NutriGenie is a GenAI-powered chatbot designed to provide smart, personalized nutrition advice based on your **age**, **goals**, and **dietary preferences**.

Whether you're diabetic, vegetarian, a gym-goer, or just trying to eat clean — NutriGenie understands your profile and helps answer:
- “Can I eat jackfruit if I'm diabetic?”
- “Suggest a high-protein breakfast”
- “Compare tofu vs paneer for weight loss”

---

## 🧠 Key Features

- 🧾 **Profile-Aware Responses** – Considers age, weight goals, and dietary needs
- 📄 **PDF-Guided Answers** – Uses RAG with real nutritional documents
- 🤖 **Natural Conversations** – Ask in plain language
- 🌐 **Live App** – [Try it here](https://nutrigenie.streamlit.app)

---

## 🧰 Tech Stack

- **LangChain** for LLM & agents
- **Streamlit** for front-end deployment
- **FAISS** for vector search
- **RAG** (Retrieval-Augmented Generation)
- **GROQ LLM API** (Mistral-7B)
- **HuggingFace Transformers** + **Sentence Transformers**
- **Python** + **PDF-based QA**

---

## 🚀 Getting Started (Local Setup)

```bash
git clone https://github.com/nabilshajahan3110/NutriGenie.git
cd NutriGenie
pip install -r requirements.txt
