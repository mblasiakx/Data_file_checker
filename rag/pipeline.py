def format_contexts(contexts: list[str]) -> str:
    return "\n".join([f"[{i+1}] {c.strip()}" for i, c in enumerate(contexts)])

def format_contexts_with_line_numbers(contexts: list[str]) -> str:
    return "\n".join([f"[{i+1}] {ctx}" for i, ctx in enumerate(contexts)])



def run_qa(llm_chain, retriever, questions):
    qa_data = []
    for q in questions:
        result = llm_chain.invoke({"query": q["question"]})
        raw_contexts = [doc.page_content for doc in retriever.invoke(q["question"])]
      
        
        qa_data.append({
            "question": q["question"],
            "answer": result["result"],
            "retrieved_contexts": raw_contexts,  # dla ragas
            "formatted_contexts": format_contexts_with_line_numbers(raw_contexts),
            "reference": q["reference"]
        })
    return qa_data