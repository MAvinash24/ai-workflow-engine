# src/memory/history_tracker.py

from datetime import datetime

history = []

def add_history(goal, step, result, evaluation):
    history.append({
        "timestamp": datetime.now().isoformat(),
        "goal": goal,
        "step": step,
        "result": str(result),
        "evaluation": evaluation
    })

def get_history():
    return history

def clear_history():
    history.clear()