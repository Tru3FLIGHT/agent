from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt

MODEL = "gemini-2.5-flash"

def query_model(client, messages, verbose=False, root_directory=None)-> str:
    for _ in range(20): # Limiting iterations per user turn to prevent infinite loops

        #gen response
        response = client.models.generate_content(
                model=MODEL,
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],system_instruction=system_prompt))


        if response.usage_metadata == None:
            raise RuntimeError("Possible api error - no usage metadata")

        if not response.candidates:
            print("No candidates in this iteration. Continuing...")
            break # Exit the inner loop if no candidates, allow new user input
        for candidate in response.candidates:
            messages.append(candidate.content)

        if verbose:
            print(f"""
    Iteration: {_}

    Prompt tokens: {response.usage_metadata.prompt_token_count}

    Response tokens: {response.usage_metadata.candidates_token_count}

    =====

              """)

        result_list = []
        #find function calls
        #if any function calls are detected, call_function, root dir declaired in call_function.py
        if response.function_calls:
            for call in response.function_calls:
                call_result = call_function(call, verbose, root_directory=root_directory)
                if call_result.parts:
                    func_response = call_result.parts[0].function_response
                    if not func_response:
                        raise Exception("function response cannot be NoneType")
                    fr_response = func_response.response
                    if not fr_response:
                        raise Exception("Response property of function_response cannot be NoneType")
                    result_list.append(call_result.parts[0])
                    if verbose:
                        print(f"-> {fr_response}")
                else:
                    raise Exception(f"CRITICAL ERROR: {call_result} has empty parts list")
        else:
            return response.text # Exit the inner loop if no function calls, display text response

        messages.append(types.Content(role="user", parts=result_list))
    return "Warning: Max iterations reached for this turn."
