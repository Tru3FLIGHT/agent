from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt


def run_chatbot_session(client, messages, verbose=False, root_directory=None):
    """
    Runs the main chatbot interaction loop.

    Args:
        client: The Generative AI client instance.
        messages: The list of conversation messages.
        verbose: A boolean indicating whether to enable verbose output.
        root_directory: An optional string specifying the root directory for file operations.
    """
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() == 'exit':
            print("Ending conversation.")
            break

        messages.append(types.Content(role="user", parts=[types.Part(text=user_prompt)]))
