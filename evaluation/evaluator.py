from ragas.evaluation import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset  # <-- TO JEST KLUCZ
import pandas as pd

def evaluate_answers(qa_data):
    # 1. Stwórz pandas DataFrame z Twoich wyników
    df = pd.DataFrame(qa_data)

    # 2. Zamień na Dataset z HuggingFace
    dataset = Dataset.from_pandas(df)

    # 3. Wywołaj evaluate z poprawnym typem danych
    results = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision]
    )

    # 4. Zwróć DataFrame z wynikami metryk
    return results.to_pandas()