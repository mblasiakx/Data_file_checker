from ragas.evaluation import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall 



from sklearn.metrics import recall_score
from datasets import Dataset  
import pandas as pd

def evaluate_answers(qa_data):
    df = pd.DataFrame(qa_data)
    dataset = Dataset.from_pandas(df)
    results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
    )

    return results.to_pandas()