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
Activate the virtual environment

Windows:

bash
Copy code
venv\Scripts\activate
Mac/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
