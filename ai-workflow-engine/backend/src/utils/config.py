# src/utils/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    API_TIMEOUT = 10
    MAX_STEPS = 10