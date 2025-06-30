import ragas.llms.base as base
from langchain_ollama import OllamaLLM

base.llm_factory = lambda: OllamaLLM(model="gemma3:1b")

import pandas as pd
from ragas.evaluation import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

def evaluate_answers(qa_data):
    data_to_evaluate = pd.DataFrame(qa_data)
    results = evaluate(
        data_to_evaluate,
        metrics=[faithfulness, answer_relevancy, context_precision]
    )
    return results.to_pandas()