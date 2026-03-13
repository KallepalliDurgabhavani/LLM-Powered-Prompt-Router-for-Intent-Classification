import json
import logging
from typing import Dict, Any
import google.generativeai as genai
from .config import GOOGLE_API_KEY, CLASSIFIER_MODEL

logger = logging.getLogger(__name__)

DEFAULT_INTENT = {"intent": "unclear", "confidence": 0.0}

def classify_intent(message: str) -> Dict[str, Any]:
    """
    Classifies the user's intent based on their message using Gemini structured output.
    """
    if not GOOGLE_API_KEY:
        logger.error("GOOGLE_API_KEY not found.")
        return DEFAULT_INTENT

    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Define the response schema
    response_schema = {
        "type": "object",
        "properties": {
            "intent": {
                "type": "string",
                "enum": ["code", "data", "writing", "career", "unclear"]
            },
            "confidence": {
                "type": "number"
            }
        },
        "required": ["intent", "confidence"]
    }

    system_prompt = (
        "Your task is to classify the user's intent. Based on the user message below, "
        "choose one of the following labels: code, data, writing, career, unclear. "
        "Respond with a JSON object containing 'intent' and 'confidence'."
    )

    try:
        model = genai.GenerativeModel(
            model_name=CLASSIFIER_MODEL,
            system_instruction=system_prompt
        )
        
        response = model.generate_content(
            message,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=response_schema
            )
        )
        
        intent_data = json.loads(response.text)
        
        # Ensure intent is lowercase for matching
        intent_data["intent"] = str(intent_data["intent"]).lower()
        
        return intent_data
    except Exception as e:
        logger.warning(f"Error classifying intent with Gemini: {e}. Defaulting to unclear.")
        return DEFAULT_INTENT
