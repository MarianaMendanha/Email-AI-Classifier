from llama_index.llms.ollama import Ollama


def get_llm(json_mode=False):
    return Ollama(
        model="llama3.1:8b",
        request_timeout=240.0,
        context_window=10000,
        json_mode=json_mode,
    )
