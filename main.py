import os
from google import genai
from dotenv import load_dotenv
import argparse

import chatbot_core
import conversation_manager

def main():

    #parsing input.....
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-n", "--new-conversation", action="store_true", help="Start a new conversation, ignoring previous history")
    parser.add_argument("--root-directory", type=str, default=None, help="Specify an alternative root directory for file operations.") # <--- ADDED THIS LINE
    args = parser.parse_args()

    #loading env and api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("api key not found")
    client = genai.Client(api_key=api_key)

    messages = []

    # Load conversation history or start new, based on argument
    if args.new_conversation:
        print("Starting a new conversation as requested.")
    else:
        messages = conversation_manager.load_conversation_history()

    print("Agent started. Type 'exit' to end the conversation.")

    # Call the chatbot_core function to handle the main interaction
    chatbot_core.run_chatbot_session(client, messages, args.verbose, args.root_directory) # <--- MODIFIED THIS LINE

    # Save conversation history before exiting
    conversation_manager.save_conversation_history(messages)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        quit(1)