import os
import subprocess
from functions.path_validation import validate_path
from google.genai import types

def run_python_file(working_directory, directory, args=None):
    try:
        wdp, target = validate_path(working_directory, directory)

        if not target.endswith(".py"):
            return f"Error: \"{directory}\" is not a Python file"
        command = ["python", target]
        
        if args != None:
            command.extend(args)

        comp_process = subprocess.run(command, capture_output=True, cwd=os.path.dirname(target), text=True, timeout=30)
        output = ""
        if comp_process.returncode != 0:
            output += f"Process exited with code {comp_process.returncode}\n"
        if (comp_process.stdout == None) and (comp_process.stderr == None):
            output += f"No output produced"
        elif comp_process.stdout:
            output += f"STDOUT:{comp_process.stdout}"
        elif comp_process.stderr:
            output += f"STDERR:{comp_process.stderr}"
        return output
    except Exception as e:
        return f"Error: executing python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a specified python file reletive to the working directory",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="File path of the python file to execute"
                    ),
                "args": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(
                        type=types.Type.STRING,
                        ),
                    description="A List of Strings for file arguments"
                    ),
                },
            required=["directory"]
            ),
        )
