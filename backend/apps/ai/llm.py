import os
from llama_index.llms.ollama import Ollama
# Importante: verifique se está no requirements
from llama_index.llms.groq import Groq


def get_llm(json_mode=False):
    # Se existir a chave do Groq no ambiente, usa o Groq (Produção/Railway)
    groq_key = os.getenv("GROQ_API_KEY")

    if groq_key:
        return Groq(
            model="llama-3.3-70b-versatile",
            api_key=groq_key,
            request_timeout=240.0,
            json_mode=json_mode,
        )

    # Caso contrário, usa o Ollama (Desenvolvimento Local)
    return Ollama(
        model="llama3.1:8b",
        request_timeout=240.0,
        context_window=10000,
        json_mode=json_mode,
    )
