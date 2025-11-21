import pandas as pd
import os
from config import Config

def load_and_preprocess(csv_path, save_path="preprocessed_movies.csv"):
    df = pd.read_csv(csv_path)

    # Keep only Title and Plot, drop rows with missing data
    df = df[['Title', 'Plot']]
    df = df.dropna(subset=['Title', 'Plot'])
    df = df[df['Plot'].str.len() > 50]

    # Randomly sample a subset
    df = df.sample(n=Config.SUBSET_SIZE, random_state=42).reset_index(drop=True)

    # Save preprocessed CSV
    df.to_csv(save_path, index=False)
    print(f"Preprocessed CSV saved to: {os.path.abspath(save_path)}")

    return df

def chunk_text(text, chunk_size, overlap):
    words = text.split()
    step = chunk_size - overlap
    for i in range(0, len(words), step):
        yield " ".join(words[i:i + chunk_size])

def create_chunks(df):
    chunks = []
    for _, row in df.iterrows():
        for c in chunk_text(row["Plot"], Config.CHUNK_SIZE, Config.CHUNK_OVERLAP):
            chunks.append({
                "title": row["Title"],
                "chunk": c
            })
    return chunks
