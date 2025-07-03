This project implements a Retrieval-Augmented Generation (RAG) pipeline for querying text files and evaluating the quality of answers using the ragas evaluation framework and Ollama LLM. It demonstrates how to:

Load and split large text files into chunks

Create a vector retriever with HuggingFace embeddings and FAISS

Generate answers using a local LLM via Ollama

Evaluate answers using ragas metrics with OpenAI's GPT-3.5-turbo

Export evaluation results to CSV for analysis
