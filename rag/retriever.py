from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_retriever(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    retriever = FAISS.from_texts(chunks, embedding=embeddings)
    return retriever.as_retriever(search_kwargs={"k": 3}) 
