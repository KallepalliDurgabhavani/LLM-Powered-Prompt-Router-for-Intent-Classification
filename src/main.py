import logging
from .classifier import classify_intent
from .responder import route_and_respond
from .logger_utils import log_interaction

logger = logging.getLogger(__name__)

def process_message(message: str) -> str:
    """
    Main orchestration function: Classify -> Route & Respond -> Log.
    """
    # 1. Classify intent
    intent_data = classify_intent(message)
    print("Intent Data: ", intent_data)
    
    # 2. Route to specialized persona and generate response
    response = route_and_respond(message, intent_data)
    
    # 3. Log the interaction
    log_interaction(message, intent_data, response)
    
    return response

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
        print(process_message(user_message))
    else:
        print("Usage: python main.py <message>")
