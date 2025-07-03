from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

model_name = "gemma3:1b"
def create_chain(model_name:str, retriever):
    llm = OllamaLLM(model=model_name)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


