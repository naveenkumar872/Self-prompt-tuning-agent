# controller.py
from executer import run_task
from evaluator import evaluate_output
from tuner import tune_prompt
from memory import save_run

def self_tuning_loop(user_input: str,base_prompt: str,score_threshold: int = 90,max_attempts: int = 3):
    current_prompt = base_prompt
    all_attempts = []

    for attempt in range(1, max_attempts + 1):
        print(f"\n🔁 Attempt {attempt}")

        # 1. Generate output
        output = run_task(user_input, current_prompt)
        print("📤 Output:", output)

        # 2. Evaluate output
        feedback = evaluate_output(user_input,output)
        print("📝 Evaluation:", feedback)
        
        run_data = {
            "attempt": attempt,
            "input": user_input,
            "prompt": current_prompt,
            "output": output,
            "score": feedback["score"],
            "reason": feedback["reason"]
        }
        # 3. Log the run
        save_run(run_data)
        all_attempts.append(run_data)

        # 4. If score is good enough, stop
        if feedback["score"] >= score_threshold:
            print("✅ Good enough! Done.")
            return output,feedback,all_attempts

        # 5. Tune the prompt for next attempt
        current_prompt = tune_prompt(
            input=user_input,
            prompt=current_prompt,
            output=output,
            score=feedback["score"],
            reason=feedback["reason"]
        )
        print("🎯 New Prompt:\n", current_prompt)

    print("❌ Max attempts reached. Final output:")
    
    return output,feedback,all_attempts


def process_input(user_input: str):
    default_prompt = "You are a helpful assistant. Complete the following task:\n\n{input}"
    final_output,feedback,all_attempts = self_tuning_loop(user_input=user_input, base_prompt=default_prompt)
    return final_output,feedback,all_attempts 