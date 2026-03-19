import json
import os
from google.genai import types

CONVERSATION_FILE = "conversation_history.json"

def load_conversation_history():
    """
    Loads conversation history from a JSON file.

    Returns:
        list: A list of google.genai.types.Content objects representing the conversation.
    """
    messages = []
    if os.path.exists(CONVERSATION_FILE):
        try:
            with open(CONVERSATION_FILE, 'r') as f:
                saved_messages = json.load(f)
                for msg in saved_messages:
                    role = msg['role']
                    parts = []
                    for part_data in msg['parts']:
                        if 'text' in part_data:
                            parts.append(types.Part(text=part_data['text']))
                        elif 'function_call' in part_data:
                            function_call_data = part_data['function_call']
                            parts.append(types.Part(function_call=types.FunctionCall(
                                name=function_call_data['name'],
                                args=function_call_data['args']
                            )))
                        elif 'function_response' in part_data:
                            function_response_data = part_data['function_response']
                            parts.append(types.Part(function_response=types.FunctionResponse(
                                name=function_response_data['name'],
                                response=function_response_data['response']
                            )))
                    messages.append(types.Content(role=role, parts=parts))
            print(f"Loaded previous conversation from {CONVERSATION_FILE}.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {CONVERSATION_FILE}. Starting a new conversation.")
        except Exception as e:
            print(f"An error occurred while loading conversation: {e}. Starting a new conversation.")
    return messages

def save_conversation_history(messages):
    """
    Saves conversation history to a JSON file.

    Args:
        messages: A list of google.genai.types.Content objects to save.
    """
    try:
        with open(CONVERSATION_FILE, 'w') as f:
            serializable_messages = []
            for msg in messages:
                serializable_parts = []
                for part in msg.parts:
                    if part.text:
                        serializable_parts.append({'text': part.text})
                    elif part.function_call:
                        serializable_parts.append({
                            'function_call': {
                                'name': part.function_call.name,
                                'args': part.function_call.args
                            }
                        })
                    elif part.function_response:
                        serializable_parts.append({
                            'function_response': {
                                'name': part.function_response.name,
                                'response': part.function_response.response
                            }
                        })
                serializable_messages.append({'role': msg.role, 'parts': serializable_parts})
            json.dump(serializable_messages, f, indent=4)
        print(f"Conversation saved to {CONVERSATION_FILE}.")
    except Exception as e:
        print(f"An error occurred while saving conversation: {e}")