
# tuner.py
from llm import call_ollama

TUNER_PROMPT_TEMPLATE = """
You are a strict prompt rewriter agent.

You will receive:
- A user task
- The original prompt used
- The LLM's output
- Feedback with score and reason

Your only job is to rewrite the original prompt to improve the quality of future outputs.

🛑 RULES:
- Do NOT say things like "Sure", "Here's an improved prompt", or any explanation.
- Do NOT include "--- Prompt ---", "--- Output Expected ---", or formatting.
- Do NOT generate the output to the prompt.
- Return only ONE LINE: the improved prompt only. Nothing else.

--- USER INPUT ---
{input}

--- ORIGINAL PROMPT ---
{prompt}

--- OUTPUT GENERATED ---
{output}

--- FEEDBACK ---
Score: {score}
Reason: {reason}

Return ONLY the improved prompt:

For Example:
You are a helpful assistant. Complete the following task: ..........

Note: Only include the improved prompt and avoid extra words other than the improved prompt
"""

def tune_prompt(input: str, prompt: str, output: str, score: int, reason: str, model: str = "mistral:7b-instruct") -> str:
    tuning_prompt = TUNER_PROMPT_TEMPLATE.format(
        input=input,
        prompt=prompt,
        output=output,
        score=score,
        reason=reason
    )
    return call_ollama(prompt=tuning_prompt, model=model)


 