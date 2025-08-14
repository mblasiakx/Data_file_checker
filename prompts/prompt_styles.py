
base_questions = [
    {
        "question": "What tournament was before Champions League?",
        "reference": "European Cup was tournament before Champions League."
    },

    {
        "question": "Until what year was the European Cup played?",
        "reference": "European Cup was played until 1992."
    },

    {
        "question": "Since when the Champions League started to be played?",
        "reference": "Champions League started to be played from 1992."
    },

    {
        "question": "What is a difference between Champions League and European Cup?",
        "reference": "Champions League has different format that European Cup."
    },

    {
        "question": "Which club has the most wins in the Champions League?",
        "reference": "Real Madrid has the most wins in the Champions League."
    },

    {
        "question": "How many times Real Madrid won European Cup?",
        "reference": "Real Madrid won European Cup 6 times."
    },

    {
        "question": "How many years after first edition of Champions League tournament was extended to 16 teams?",
        "reference": "Champions League was extended to 16 teams after 2 years."
    },

    {
        "question": "How many teams participated in the first edition of the Champions League?",
        "reference": "In the first edition of the Champions League 8 teams were playing."
    },

    {
        "question": "What is a Real Madrid?",
        "reference": "Real Madrid is a football team."
    },
     
    {
        "question": "How many teams from Poland won Champions League?",
        "reference": "No team from Poland won Champions League."
    },

    {
        "question": "What is the area of Canada?",
        "reference": "Canada has 9,984,670 square kilometers."
    },
]


def format_zero_shot(q):
    return q["question"]

def format_one_shot(q):
    ONE_SHOT_EXAMPLE = """Q: What is the Champions League?
    A:Champions League is the football tournament for clubs from many countries"
    """
    return ONE_SHOT_EXAMPLE + f"\nQ: {q['question']}\nA:"

def format_few_shot(q):
    FEW_SHOT_EXAMPLE = """Q: What is the Champions League?
    A:Champions League is the football tournament for clubs from many countries"

    Q: How often Champions League is played?
    A: Champions League is played every year"
    """
    return FEW_SHOT_EXAMPLE + f"\nQ: {q['question']}\nA:"

def format_cot(q):
    return f"{q['question']} Let's think step by step."

def format_prompt_injection(q):
    return f"You are a football analyst. Answer the question truthfully and precisely: {q['question']}"