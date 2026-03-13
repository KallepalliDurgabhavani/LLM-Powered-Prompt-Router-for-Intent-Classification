import logging
from typing import Dict, Any
import google.generativeai as genai
from .config import GOOGLE_API_KEY, MODEL_NAME, SYSTEM_PROMPTS

logger = logging.getLogger(__name__)

def route_and_respond(message: str, intent_data: Dict[str, Any]) -> str:
    """
    Routes the message to the appropriate expert or asks for clarification using Gemini.
    """
    if not GOOGLE_API_KEY:
        logger.error("GOOGLE_API_KEY not found.")
        return "I encountered an error. Please check the configuration."

    genai.configure(api_key=GOOGLE_API_KEY)
    
    intent = intent_data.get("intent", "unclear")
    confidence = intent_data.get("confidence", 0.0)

    # Handle unclear intent or low confidence
    if intent == "unclear" or confidence < 0.6:
        return (
            "I'm not sure I understand what you're looking for. "
            "Are you asking for help with coding, data analysis, writing, or career advice?"
        )

    # Get specialized prompt
    system_prompt = SYSTEM_PROMPTS.get(intent)
    if not system_prompt:
        return (
            "I'm not sure I understand what you're looking for. "
            "Are you asking for help with coding, data analysis, writing, or career advice?"
        )

    try:
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=system_prompt
        )
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        logger.error(f"Error generating response with Gemini: {e}")
        return "I encountered an error while processing your request. Please try again later."
