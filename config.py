import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBED_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-4o-mini"

    CHUNK_SIZE = 300
    CHUNK_OVERLAP = int(CHUNK_SIZE * 0.1)  # 10% overlap
    TOP_K = 3
    SUBSET_SIZE = 350
    EMBED_DIM = 1536

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set. Add it to your .env file.")
