import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import argparse
from prompts import *
from call_function import available_functions


MODEL = "gemini-2.5-flash"

def main():
    
    #parsing input.....
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    #loading env and api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("api key not found")
    client = genai.Client(api_key=api_key)
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

                                                                   #gen response
    response = client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[system_instruction=system_prompt))
    
    if response.usage_metadata == None:
        raise RuntimeError("Possible api error - no usage metadata")

    if args.verbose:
        print(f"\
User prompt: {args.user_prompt}\n\
Prompt tokens: {response.usage_metadata.prompt_token_count}\n\
Response tokens: {response.usage_metadata.candidates_token_count}\n\
=====\n")

    print(f"{response.text}")

    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        quit(1)
