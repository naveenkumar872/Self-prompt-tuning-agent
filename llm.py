import requests


def call_ollama(prompt: str, model: str = "llama2", stream: bool = False) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["response"]

    except requests.RequestException as e:
        print(f"Error calling Ollama: {e}")
        return "Error"


