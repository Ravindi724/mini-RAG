from retriever import retrieve_chunks
from llm_handler import generate_answer

def answer_query(query, chunks, index):
    retrieved = retrieve_chunks(query, chunks, index)
    result = generate_answer(query, retrieved)
    return result
