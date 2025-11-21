from data_loader import load_and_preprocess, create_chunks
from vector_store import build_faiss_index
from rag_pipeline import answer_query

import json

if __name__ == "__main__":
    # Load and preprocess data
    df = load_and_preprocess(
        r"C:\Users\Ravindi Hewage\Desktop\Snapdrum\wiki_movie_plots_deduped.csv",
        save_path="preprocessed_movies.csv"
    )
    print("Loaded and cleaned:", len(df), "rows")

    # Create chunks with overlap
    chunks = create_chunks(df)
    print("Generated", len(chunks), "chunks")

    # Build FAISS index
    print("Building FAISS index (embedding all chunks)...")
    index = build_faiss_index(chunks)
    print("FAISS index ready!")

    # Interactive QA loop
    print("\n--- Movie Plot QA (type 'exit' to quit) ---")
    while True:
        query = input("\nEnter your movie question: ")
        if query.strip().lower() in ["exit", "quit"]:
            print("Exiting.")
            break

        output = answer_query(query, chunks, index)
        print("\nStructured JSON output:")
        print(json.dumps(output, indent=4))
