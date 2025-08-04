import ragas.llms.base as base
from langchain_ollama import OllamaLLM
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.file_loader import load_document
from rag.splitter import split_text_form_file
from rag.retriever import create_retriever
from rag.generator import create_chain
from rag.pipeline import run_qa
from evaluation.evaluator import evaluate_answers

load_dotenv()
questions = [
    {
        "question": "Who is owner of Lyon?",
        "reference": "John Textor is the owner of Lyon."
    },
    {
        "question": "Which club has hope to play in the Europa League next season?",
        "reference": "Cristal Palace has hope to play in the Europa League next season."
    },
    {
        "question": "Why Lyon has been relegated?",
        "reference": "Lyon has not been relegated; the question is based on a false assumption."
    },

    {
        "question": "Which quarter of a year Eagle Football Group announced debts of £422m?",
        "reference": "On fourth quarter of a year Eagle Football Group announced debts of £422m."
    }
]


#text = load_file("data/Lyon.txt")
text= load_document("data/Lyon.docx")
chunks = split_text_form_file(text)
retriever = create_retriever(chunks)
llm_chain = create_chain("gemma3:1b", retriever)
qa_data = run_qa(llm_chain, retriever, questions)

results_df = evaluate_answers(qa_data)
results_df.to_csv("evaluation/results/evaluation.csv", index=False)
print(results_df)


