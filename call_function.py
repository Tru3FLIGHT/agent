from functions import get_files_info as gfi
from functions import get_file_content as ctn
from functions import run_python_file as rpf
from functions import write_file as wf
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types

available_functions = types.Tool(
        function_declarations=[gfi.schema_get_files_info, ctn.schema_get_file_content, wf.schema_write_file],)

function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
        }

def call_function(func_call, verbose=False, root_directory=None): # <--- MODIFIED FUNCTION SIGNATURE
    if verbose:
        print(f"Calling function: {func_call.name}({func_call.args})")
    else:
        print(f" - Calling Function: {func_call.name}\n")
    
    function_name = func_call.name or ""

    if function_name not in function_map:
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                        )
                    ],
                )

    args = dict(func_call.args) if func_call.args else {}

    # Use the provided root_directory or fallback to the hardcoded one
    if root_directory: # <--- ADDED THIS BLOCK
        args["working_directory"] = root_directory
    else:
        args["working_directory"] = "/home/zalea/Documents/Projects/bootdev/assignments/agent"

    try:
        function_result = function_map[function_name](**args)
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                        )
                    ],
                )
    except Exception as e:
        error_message = f"Error executing function {function_name}: {e}"
        if verbose:
            print(f"Function call failed: {error_message}")
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": error_message},
                        )
                    ],
                )