
# memory.py
import json
from datetime import datetime
from typing import Dict, List

MEMORY_FILE = "run_memory.jsonl"

def save_run(run_data: Dict, path: str = MEMORY_FILE):
    run_data["timestamp"] = datetime.now().isoformat()
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(run_data) + "\n")

def load_all_runs(path: str = MEMORY_FILE) -> List[Dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f.readlines()]
    except FileNotFoundError:
        return []


