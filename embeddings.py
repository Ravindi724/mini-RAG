import numpy as np
from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def get_embedding(text):
    resp = client.embeddings.create(
        model=Config.EMBED_MODEL,
        input=text
    )
    return np.array(resp.data[0].embedding, dtype='float32')
