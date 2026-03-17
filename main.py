import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import argparse
from prompts import *
from call_function import available_functions
from call_function import call_function


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
                tools=[available_functions],system_instruction=system_prompt))
    
    if response.usage_metadata == None:
        raise RuntimeError("Possible api error - no usage metadata")

    if args.verbose:
        print(f"\
User prompt: {args.user_prompt}\n\
Prompt tokens: {response.usage_metadata.prompt_token_count}\n\
Response tokens: {response.usage_metadata.candidates_token_count}\n\
=====\n")

    result_list = []
    if response.function_calls:
        for call in response.function_calls:
            call_result = call_function(call, args.verbose)
            if call_result.parts:
                func_response = call_result.parts[0].function_response
                if not func_response:
                    raise Exception("function response cannot be NoneType")
                fr_response = func_response.response
                if not fr_response:
                    raise Exception("Response property of function_response cannot be NoneType")
                result_list.append(call_result.parts[0])
                if args.verbose:
                    print(f"-> {fr_response}")
            else:
                raise Exception(f"CRITICAL ERROR: {call_result} has empty parts list")
    else:
        print(response.text)
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        quit(1)
