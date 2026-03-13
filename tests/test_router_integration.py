import os
import sys
import time

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import process_message

def run_tests():
    test_messages = [
        "how do i sort a list of objects in python?",
        "explain this sql query for me",
        "This paragraph sounds awkward, can you help me fix it?",
        "I'm preparing for a job interview, any tips?",
        "what's the average of these numbers: 12, 45, 23, 67, 34",
        "Help me make this better.",
        "I need to write a function that takes a user id and returns their profile, but also i need help with my resume.",
        "hey",
        "Can you write me a poem about clouds?",
        "Rewrite this sentence to be more professional.",
        "I'm not sure what to do with my career.",
        "what is a pivot table",
        "fxi thsi bug pls: for i in range(10) print(i)",
        "How do I structure a cover letter?",
        "My boss says my writing is too verbose."
    ]

    print(f"Starting tests with {len(test_messages)} messages...\n")

    for i, message in enumerate(test_messages, 1):
        print(f"Test {i}: {message}")
        try:
            print("Processing...")
            response = process_message(message)
            print(f"Response: {response[:100]}...\n")
            # time.sleep(61)
            
            # print("Simulation: Calling process_message(message)...")
            # print("Skipping actual LLM call in test script to avoid API errors if key is missing.\n")
        except Exception as e:
            print(f"Error: {e}\n")

    print("\nTests completed (simulation). Check route_log.jsonl if you ran it for real.")

if __name__ == "__main__":
    run_tests()
