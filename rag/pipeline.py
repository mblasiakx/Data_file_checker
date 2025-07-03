def run_qa(llm_chain, retriever, questions):
    qa_data = []
    for q in questions:
        result = llm_chain.invoke({"query": q["question"]})
        qa_data.append({
            "question": q["question"],
            "answer": result["result"],
            "retrieved_contexts": [doc.page_content for doc in retriever.invoke(q["question"])],
            "reference": q["reference"]
        })
    return qa_data