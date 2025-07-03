from ragas.evaluation import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset  
import pandas as pd

def evaluate_answers(qa_data):
    df = pd.DataFrame(qa_data)
    dataset = Dataset.from_pandas(df)
    results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision]
    )

    return results.to_pandas()