


base_questions = [
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
        "reference": "Lyon has not been relegated because of bad finacial condition."
    },

    {
        "question": "Which quarter of a year Eagle Football Group announced debts of £422m?",
        "reference": "On fourth quarter of a year Eagle Football Group announced debts of £422m."
    }
]


def format_zero_shot(q):
    return q["question"]

def format_one_shot(q):
    ONE_SHOT_EXAMPLE = """Q: What is the oldest club in France?
    A: Le Havre Athletic Club is the oldest football club in France"
    """
    return ONE_SHOT_EXAMPLE + f"\nQ: {q['question']}\nA:"

def format_few_shot(q):
    FEW_SHOT_EXAMPLE = """Q: What is the oldest club in France?
    A: Le Havre Athletic Club is the oldest football club in France"

    Q: Which football team in France won the most league titles?
    A: PSG is the most successful club with 13 league titles"
    """
    return FEW_SHOT_EXAMPLE + f"\nQ: {q['question']}\nA:"

def format_cot(q):
    return f"{q['question']} Let's think step by step."

def format_prompt_injection(q):
    return f"You are a football analyst. Answer the question truthfully and precisely: {q['question']}"