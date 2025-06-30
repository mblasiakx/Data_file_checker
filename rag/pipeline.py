def run_qa(llm_chain, retriever,questions):
    qa_data=[]
    for q in questions:
        result = llm_chain.invoke({"query": q})
    qa_data.append({
        "question": q,
        "answer": result["result"],
        "context": [doc.page_content for doc in retriever.invoke(q)]
    })

    return qa_data
