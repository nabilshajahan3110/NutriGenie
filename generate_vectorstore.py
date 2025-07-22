from modules.rag_engine import load_docs, build_vector_store, save_vectorstore

pdf_path = "data/diabetes_guidelines.pdf"

print("🔄 Loading PDF...")
docs = load_docs(pdf_path)

print("🔨 Building vectorstore...")
vectorstore = build_vector_store(docs)

print("💾 Saving to data/vectorstore.pkl")
save_vectorstore(vectorstore)

print("✅ Done!")