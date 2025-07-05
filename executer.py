# executor.py
from llm import call_ollama

# Basic default prompt template
DEFAULT_PROMPT = "You are a helpful assistant. Complete the following task:\n\n{input}"

def run_task(user_input: str, prompt_template: str = DEFAULT_PROMPT) -> str:
    final_prompt = prompt_template.format(input=user_input)
    response = call_ollama(prompt=final_prompt)
    return response


