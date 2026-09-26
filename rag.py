import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings # Embedding: To convert Date --> Numbers
from langchain_community.vectorstores import FAISS
PDF_file = "data/nutrition.pdf"

## FAISS --> Vector Database
## What is a Vector_Database? 
## Database, where instead of data, binary value of the data is stored. 

def create_rag():
    if not os.path.exists(PDF_file):
        raise FileNotFoundError("PDF file not found")
    else:
        document = PyPDFLoader(PDF_file).load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap = 50)
        chunks = splitter.split_documents(document)
        embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.from_documents(chunks, embeddings)
        db.save_local("vector_db") 
        return len(chunks)       

def load_rag():
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization = True)
    return db