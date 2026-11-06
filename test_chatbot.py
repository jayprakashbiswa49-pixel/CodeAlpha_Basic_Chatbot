"""
Automated Test Suite for Rule-Based Chatbot
==========================================
Tests the core functional requirements, input processing, and edge cases.
"""

from chatbot import get_response


def test_chatbot_responses():
    print("Running Chatbot Unit Tests...\n")
    test_cases = [
        # (Input, Expected Response, Description)
        # 1. Greetings
        ("hello", "Hi! How can I help you?", "Basic greeting: hello"),
        ("hi", "Hi! How can I help you?", "Basic greeting: hi"),
        ("hey", "Hi! How can I help you?", "Basic greeting: hey"),
        ("HELLO", "Hi! How can I help you?", "Uppercase greeting: HELLO"),
        ("  Hello  ", "Hi! How can I help you?", "Padded greeting: '  Hello  '"),
        ("hey!", "Hi! How can I help you?", "Punctuation greeting: hey!"),

        # 2. General Questions
        ("how are you", "I'm fine, thanks! How about you?", "Question: how are you"),
        ("How are you?", "I'm fine, thanks! How about you?", "Question with capital and question mark"),
        ("what is your name", "I'm Python Bot, your virtual assistant.", "Question: what is your name"),
        ("What Is Your Name?", "I'm Python Bot, your virtual assistant.", "Title case with question mark"),
        ("who created you", "I was created using Python.", "Question: who created you"),
        ("what can you do", "I can answer simple questions using predefined responses.", "Question: what can you do"),

        # 3. Courtesy
        ("thank you", "You're welcome!", "Courtesy: thank you"),
        ("thanks", "You're welcome!", "Courtesy: thanks"),
        ("THANKS!", "You're welcome!", "Courtesy: THANKS!"),

        # 4. Time of Day Greetings
        ("good morning", "Good morning! Have a wonderful day.", "Greeting: good morning"),
        ("Good Morning!", "Good morning! Have a wonderful day.", "Greeting: Good Morning!"),
        ("good evening", "Good evening! How can I help you?", "Greeting: good evening"),
        ("GOOD EVENING", "Good evening! How can I help you?", "Greeting: GOOD EVENING"),

        # 5. Exit Commands
        ("bye", "Goodbye! Have a great day.", "Exit command: bye"),
        ("exit", "Goodbye! Have a great day.", "Exit command: exit"),
        ("quit", "Goodbye! Have a great day.", "Exit command: quit"),
        (" BYE! ", "Goodbye! Have a great day.", "Exit command: ' BYE! '"),

        # 6. Empty Input
        ("", "Please enter a message so I can respond.", "Empty string input"),
        ("   ", "Please enter a message so I can respond.", "Whitespace-only input"),

        # 7. Unknown Messages
        ("tell me the weather", "I'm sorry, I don't understand that. Could you try something else?", "Unknown request"),
        ("xyz123", "I'm sorry, I don't understand that. Could you try something else?", "Nonsense input"),
    ]

    all_passed = True
    for idx, (user_input, expected, description) in enumerate(test_cases, 1):
        actual = get_response(user_input)
        if actual == expected:
            print(f"[PASS] Case {idx:02d}: {description}")
        else:
            print(f"[FAIL] Case {idx:02d}: {description}")
            print(f"       Input:    {repr(user_input)}")
            print(f"       Expected: {repr(expected)}")
            print(f"       Actual:   {repr(actual)}")
            all_passed = False

    print("\n" + "=" * 40)
    if all_passed:
        print("ALL 20 TEST CASES PASSED SUCCESSFULLY!")
    else:
        print("SOME TESTS FAILED.")
    print("=" * 40)
    return all_passed


if __name__ == "__main__":
    success = test_chatbot_responses()
    if not success:
        exit(1)

