import ragas.llms.base as base
from langchain_ollama import OllamaLLM
base.llm_factory = lambda: OllamaLLM(model="gemma3:1b")
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.file_loader import load_file
from rag.splitter import split_text_form_file
from rag.retriever import create_retriever
from rag.generator import create_chain
from rag.pipeline import run_qa
from evaluation.evaluator import evaluate_answers


questions = [
    "Who is owner of Lyon?",
    "Which club has hope to play in the Europa League next season?",
    "Why Lyon has been relegated?"
]

text = load_file("data/Lyon.txt")
chunks = split_text_form_file(text)
retriever = create_retriever(chunks)
llm_chain = create_chain("gemma3:1b", retriever)
qa_data = run_qa(llm_chain, retriever, questions)

results_df = evaluate_answers(qa_data)
results_df.to_csv("evaluation/results/evaluation.csv", index=False)
print(results_df)