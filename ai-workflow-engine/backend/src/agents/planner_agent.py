# src/agents/planner_agent.py

import json
import re
from src.utils.gemini_client import generate

def clean_response(text):
    if not text:
        return ""

    # remove markdown blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    return text.strip()


def safe_parse(text):
    try:
        return json.loads(text)
    except:
        try:
            text = text.replace("'", '"')
            return json.loads(text)
        except:
            return None


def create_plan(goal: str):
    prompt = f"""
    You are a planner agent.

    Convert the goal into a JSON array of steps.

    STRICT RULES:
    - Output ONLY JSON
    - No explanation
    - No markdown
    - No code blocks

    Example:
    ["step1", "step2"]

    Goal: {goal}
    """

    # 🔁 Retry mechanism
    for _ in range(3):
        raw = generate(prompt)

        cleaned = clean_response(raw)

        plan = safe_parse(cleaned)

        if plan and isinstance(plan, list):
            return plan

    # 🆘 FINAL FALLBACK (NEVER FAIL SYSTEM)
    return [f"Execute goal: {goal}"]