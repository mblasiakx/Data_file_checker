import ragas.llms.base as base
from langchain_ollama import OllamaLLM
import sys
import os
import csv
from dotenv import load_dotenv
import mlflow

mlflow.set_experiment("championsLague_and_rome_txt_no_source_question__2")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompts.prompt_styles import base_questions, format_zero_shot, format_one_shot, format_few_shot, format_cot, format_prompt_injection
from rag.file_loader import load_document
from rag.splitter import split_text_form_file
from rag.retriever import create_retriever
from rag.generator import create_chain
from rag.pipeline import run_qa
from evaluation.evaluator import evaluate_answers

from dotenv import load_dotenv
import os, sys, csv, mlflow

load_dotenv()

styles = {
    "zero_shot": format_zero_shot,
    "one_shot": format_one_shot,
    "few_shot": format_few_shot,
    "chain_of_thought": format_cot,
    "prompt_injection": format_prompt_injection,
}


use_more_files = True  


if use_more_files:
    doc1 = load_document("data/Champions League.txt")
    doc2 = load_document("data/Rome.txt")

    chunks1 = split_text_form_file(doc1)
    chunks2 = split_text_form_file(doc2)

    all_chunks = chunks1 + chunks2
else:
    doc1 = load_document("data/Champions League.txt")
    all_chunks = split_text_form_file(doc1)

retriever = create_retriever(all_chunks)
llm_chain = create_chain("gemma3:1b", retriever)


for style_name, formatter in styles.items():
    print(f"Evaluating prompt style: {style_name}")

    styled_questions = []
    for q in base_questions:
        prompt = formatter(q)
        styled_questions.append({
            "question": prompt,
            "reference": q["reference"]
        })

    qa_data = run_qa(llm_chain, retriever, styled_questions)
    embeddings = retriever.vectorstore.embedding_function

    results_df = evaluate_answers(qa_data, embeddings)
    results_df["formatted_contexts"] = [
        sample["formatted_contexts"] for sample in qa_data
    ]

    csv_path = f"evaluation/results/evaluation_{style_name}.csv"
    results_df.to_csv(csv_path, index=False, quoting=csv.QUOTE_ALL, encoding="utf-8")

    with mlflow.start_run(run_name=style_name):
        mlflow.log_param("prompt_style", style_name)
        mlflow.log_param("model_name", "gemma3:1b")
        mlflow.log_param("num_questions", len(styled_questions))

        for metric in results_df.columns:
            if results_df[metric].dtype in ["float64", "int64"]:
                mlflow.log_metric(metric, results_df[metric].mean())

        mlflow.log_artifact(csv_path)