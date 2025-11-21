import numpy as np
import faiss
from embeddings import get_embedding
from config import Config

def build_faiss_index(chunks):
    index = faiss.IndexFlatL2(Config.EMBED_DIM)
    embeddings = [get_embedding(c["chunk"]) for c in chunks]
    index.add(np.array(embeddings))
    return index
