import numpy as np
from embeddings import get_embedding
from config import Config

def retrieve_chunks(query, chunks, index):
    q_emb = get_embedding(query)
    distances, idxs = index.search(np.array([q_emb]), Config.TOP_K)
    return [chunks[i] for i in idxs[0]]
