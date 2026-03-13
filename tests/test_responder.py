import os
import sys
import unittest

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.responder import route_and_respond

class TestResponder(unittest.TestCase):
    def test_route_and_respond_unclear(self):
        # Test unclear intent
        intent_data = {"intent": "unclear", "confidence": 0.0}
        message = "hey"
        result = route_and_respond(message, intent_data)
        self.assertIn("Are you asking for help with coding", result)

    def test_route_and_respond_low_confidence(self):
        # Test low confidence
        intent_data = {"intent": "code", "confidence": 0.3}
        message = "how to code?"
        result = route_and_respond(message, intent_data)
        self.assertIn("Are you asking for help with coding", result)

if __name__ == '__main__':
    unittest.main()
