# src/tools/custom_tool.py

import random

def send_notification(message):
    return f"Notification sent: {message}"

def save_to_db(data):
    # Simulated DB save
    return {"status": "saved", "data_preview": str(data)[:100]}

def simple_scraper():
    # Fake scraping logic
    data = [
        {"title": "AI News", "content": "Latest AI trends..."},
        {"title": "Tech Update", "content": "New tools released..."}
    ]
    return data

def choose_best_option(options):
    return random.choice(options)