from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_docs(pdf_path):
    loader = PyPDFLoader(pdf_path)
    all_pages = loader.load()
    selected_pages = all_pages[:3]  # Load first 3 pages only
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(selected_pages)

def build_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(docs, embeddings)

def get_relevant_chunks(vectorstore, query, k=3):
    return vectorstore.similarity_search(query, k=k)