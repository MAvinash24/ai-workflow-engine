from src.tools.api_tool import call_api
from src.tools.custom_tool import send_notification, save_to_db
from src.utils.gemini_client import generate


def execute_step(step, context=None):
    step = step.lower()

    if "fetch" in step:
        data = call_api("https://jsonplaceholder.typicode.com/posts")
        return data

    elif "summarize" in step:
        if context:
            return generate(f"Summarize this data:\n{context}")
        return "No data to summarize"

    elif "store" in step:
        return save_to_db(context if context else {"data": "sample"})

    elif "notify" in step:
        return send_notification("Task completed")

    return f"Executed: {step}"