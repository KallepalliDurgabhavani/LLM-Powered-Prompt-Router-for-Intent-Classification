import json
import logging
from typing import Dict, Any
from .config import LOG_FILE

logger = logging.getLogger(__name__)

def log_interaction(message: str, intent_data: Dict[str, Any], response: str):
    """
    Logs the routing decision and final response to a JSON Lines file.
    """
    log_entry = {
        "intent": intent_data.get("intent"),
        "confidence": intent_data.get("confidence"),
        "user_message": message,
        "final_response": response
    }
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    except Exception as e:
        logger.error(f"Error logging request: {e}")
