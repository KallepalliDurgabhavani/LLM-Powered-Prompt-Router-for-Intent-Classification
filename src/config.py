import os
import json
import logging
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROMPTS_FILE = os.path.join(os.path.dirname(__file__), "prompts.json")
LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "route_log.jsonl")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")
CLASSIFIER_MODEL = os.getenv("CLASSIFIER_MODEL", "gemini-1.5-flash")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def load_prompts() -> Dict[str, str]:
    try:
        if not os.path.exists(PROMPTS_FILE):
            logger.error(f"{PROMPTS_FILE} not found.")
            return {}
        with open(PROMPTS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading prompts: {e}")
        return {}

SYSTEM_PROMPTS = load_prompts()
