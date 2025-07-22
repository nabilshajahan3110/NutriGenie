from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pickle

def load_docs(pdf_path):
    loader = PyPDFLoader(pdf_path)
    all_pages = loader.load()
    selected_pages = all_pages[:3]  # Only first 3 pages to save memory
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return text_splitter.split_documents(selected_pages)

def build_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)

def save_vectorstore(vectorstore, path="data/vectorstore.pkl"):
    with open(path, "wb") as f:
        pickle.dump(vectorstore, f)

def load_vectorstore(path="data/vectorstore.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)

def get_relevant_chunks(vectorstore, query, k=3):
    return vectorstore.similarity_search(query, k=k)