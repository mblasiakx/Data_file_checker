import ragas.llms.base as base
from langchain_ollama import OllamaLLM
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompts.prompt_styles import base_questions, format_zero_shot, format_few_shot, format_cot, format_prompt_injection
from rag.file_loader import load_document
from rag.splitter import split_text_form_file
from rag.retriever import create_retriever
from rag.generator import create_chain
from rag.pipeline import run_qa
from evaluation.evaluator import evaluate_answers

load_dotenv()

styles = {
    "zero_shot": format_zero_shot,
    "few_shot": format_few_shot,
    "chain_of_thought": format_cot,
    "prompt_injection": format_prompt_injection,
}

text= load_document("data/Lyon.docx")
chunks = split_text_form_file(text)
retriever = create_retriever(chunks)
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
    results_df = evaluate_answers(qa_data)
    results_df.to_csv(f"evaluation/results/evaluation_{style_name}.csv", index=False)
#print(results_df)


