"""
Rule-Based Chatbot in Python
============================
A simple interactive chatbot that communicates with users through the terminal
using predefined rules, if-elif-else statements, functions, loops, and string methods.
"""


def get_response(user_input: str) -> str:
    """
    Processes the user's input and returns a predefined response.

    Parameters:
        user_input (str): The raw or partially processed message from the user.

    Returns:
        str: The chatbot's response based on rule-based matching.
    """
    # Step 1: Normalize input - remove leading/trailing whitespaces and convert to lowercase
    cleaned_input = user_input.strip().lower()

    # Step 2: Handle empty input
    if not cleaned_input:
        return "Please enter a message so I can respond."

    # Step 3: Strip trailing punctuation (e.g. '?', '!', '.') for flexible rule matching
    normalized_input = cleaned_input.rstrip("?!.")

    # Step 4: Rule-based matching using if-elif-else conditions
    if normalized_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif normalized_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif normalized_input == "what is your name":
        return "I'm Python Bot, your virtual assistant."

    elif normalized_input == "who created you":
        return "I was created using Python."

    elif normalized_input == "what can you do":
        return "I can answer simple questions using predefined responses."

    elif normalized_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif normalized_input == "good morning":
        return "Good morning! Have a wonderful day."

    elif normalized_input == "good evening":
        return "Good evening! How can I help you?"

    elif normalized_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    else:
        # Default fallback for any unrecognized message
        return "I'm sorry, I don't understand that. Could you try something else?"


def run_chatbot() -> None:
    """
    Starts and manages the interactive terminal chatbot session.
    Controls the conversation loop, input prompting, and graceful termination.
    """
    # Display the welcome header banner
    print("====================================")
    print("       PYTHON RULE-BASED CHATBOT")
    print("====================================")
    print()
    print("Bot: Hello! Welcome to Python Bot.")
    print("Bot: You can chat with me. Type 'bye' to exit.")
    print()

    # While loop to keep the chat active until the user decides to exit
    while True:
        try:
            # Prompt the user for input
            user_message = input("You: ")
        except (KeyboardInterrupt, EOFError):
            # Gracefully handle Ctrl+C or EOF interruption
            print("\n")
            print("Bot: Goodbye! Have a great day.")
            print()
            break

        # Check for empty input (whitespace-only or empty Enter key)
        if not user_message.strip():
            print("Bot: Please type something so I can respond.\n")
            continue

        # Get response using our dedicated response function
        bot_response = get_response(user_message)

        # Display the bot's response
        print(f"Bot: {bot_response}\n")

        # Check if user message indicates an exit command
        cleaned_command = user_message.strip().lower().rstrip("?!.")
        if cleaned_command in ["bye", "exit", "quit"]:
            break

    # Display the session closure banner
    print("====================================")
    print("       CHAT SESSION ENDED")
    print("====================================")


if __name__ == "__main__":
    run_chatbot()
