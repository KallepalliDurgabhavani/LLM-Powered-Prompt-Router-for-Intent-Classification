import os
import sys
import unittest

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.classifier import classify_intent

class TestClassifier(unittest.TestCase):
    def test_classify_code(self):
        # This is a unit test that would typically mock the LLM
        # For now, it's a placeholder showing the structure
        message = "how do i sort a list in python?"
        result = classify_intent(message)
        print(result)
        pass

    def test_classify_unclear(self):
        message = "hey"
        result = classify_intent(message)
        print(result)
        pass

if __name__ == '__main__':
    unittest.main()
