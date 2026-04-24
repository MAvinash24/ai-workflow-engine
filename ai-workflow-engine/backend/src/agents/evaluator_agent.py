from src.utils.gemini_client import generate

def evaluate(step, result):
    prompt = f"""
    Step: {step}
    Result: {result}

    Evaluate if successful. Return JSON:
    {{ "status": "success/fail", "reason": "" }}
    """

    return generate(prompt)