

from llm import call_ollama
import json

EVAL_PROMPT_TEMPLATE = """
You are an impartial evaluator. Given a user task and the AI-generated response, return a quality score from 1 to 100 and explain why.

Use the following strict JSON format:
{{
  "score": "<number from 1 to 100>",
  "reason": "<brief explanation>"
}}

Here are some examples:

Task:
The Eiffel Tower is located in which city?
Response:
The Eiffel Tower is in Paris.
Output:
{{
  "score": 70,
  "reason": "Correct and concise, but could include more context like the country or tourist details."
}}

Task:
Where is the Eiffel Tower?
Response:
The Eiffel Tower is in Mars.
Output:
{{
  "score": 10,
  "reason": "The answer is factually incorrect."
}}

Now evaluate the following:

--- Task ---
\"\"\"{input}\"\"\"

--- Response ---
\"\"\"{output}\"\"\"

Return your evaluation below in strict JSON format.
"""



def evaluate_output(input: str, output: str, model: str = "mistral:7b-instruct") -> dict:
    
    eval_prompt = EVAL_PROMPT_TEMPLATE.format(input=input, output=output)
   
    raw_response = call_ollama(prompt=eval_prompt, model=model)
   
    try:
        
        parsed = json.loads(raw_response)
      
        return {
            "score": parsed.get("score", 50),
            "reason": parsed.get("reason", "No reason provided.")
        }
    except Exception:
        # fallback if not in JSON
        return {
            "score": 50,
            "reason": "Could not parse evaluation response."
        }

