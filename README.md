# ⚡ Autoprompter – Self Prompt Tuning Agent

Autoprompter is an AI-powered **self-tuning prompt agent** that automatically improves its own prompts based on response evaluations and feedback. It uses a closed feedback loop to iteratively generate better outputs from an LLM (like LLaMA 2 via Ollama) without human intervention.

## 🚀 How It Works

1. **Takes a user input task**
2. **Generates a response using a base prompt**
3. **Evaluates the output using another LLM**
4. **Tunes the prompt based on evaluation score and reason**
5. **Repeats until the output quality is good enough**

---

## 🧠 Features

- 🔁 Self-tuning loop with multiple attempts
- 📊 Built-in evaluator (LLM-based scoring system)
- 📝 Prompt rewriter using LLM
- 🧠 Memory system for logging all runs
- 💬 Flask-based UI with hidden evaluation (click to reveal)
- 🛠️ Easy to extend with RAG, preferences, or agentic flows

---

## 🖥️ Demo UI

Run the Flask server and interact with Autoprompter via a simple web interface.

```bash
python main.py
