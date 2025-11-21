# Mini RAG Pipeline

A lightweight **Retrieval-Augmented Generation (RAG)** system built using:  
- FAISS for vector search  
- OpenAI embeddings  
- OpenAI LLM model  
- Modular architecture  

## Features

- Load and preprocess long text data  
- Chunking  
- Embedding with OpenAI  
- Vector storage using FAISS  
- Top-K retrieval  
- LLM answer generation  
- Fully modular and extendable  

## Project Architecture

| File | Description |
|------|-------------|
| `config.py`      | App configuration |
| `data_loader.py` | Load raw text + chunking |
| `embeddings.py`  | Embedding generation |
| `vector_store.py`| FAISS vector DB |
| `retriever.py`   | Retrieve top K chunks |
| `llm_handler.py` | Generate final answer |
| `rag_pipeline.py`| Orchestrates all steps |
| `main.py`        | CLI entry point |

## Installation

1. **Create a virtual environment**  
```bash
python -m venv venv

2. **Activate the virtual environment**
Activate the virtual environment

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Create .env file
Copy .env.example and rename it:
OPENAI_API_KEY=your_key_here

Running the Pipeline (CLI)
python main.py

You will be asked:
Enter your question:

(Type anything about your uploaded text dataset and the RAG system will answer using retrieval + generation.)
