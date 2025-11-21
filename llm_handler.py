import json
from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_answer(query, retrieved_chunks):
    context_snippets = [" ".join(c['chunk'].split()[:150]) for c in retrieved_chunks]
    context_text = "\n---\n".join(context_snippets)

    prompt = f"""
You are a helpful, concise assistant. Use ONLY the context below to answer the question.  
Do not add any external information or personal opinions.  

Context:
{context_text}

Question: {query}

Please respond in JSON format exactly as follows:
{{
  "answer": "your natural language answer here",
  "contexts": ["relevant context snippets here"],
  "reasoning": "a short explanation of how you used the context to form the answer"
}}
Do NOT include any text outside the JSON.
"""

    resp = client.chat.completions.create(
        model=Config.LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    text = resp.choices[0].message.content

    try:
        result = json.loads(text)
    except:
        result = {
            "answer": text,
            "contexts": context_snippets,
            "reasoning": "Used the retrieved chunks to form the answer."
        }

    if "contexts" not in result:
        result["contexts"] = context_snippets

    return result
