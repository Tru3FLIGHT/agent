import os
from functions.path_validation import validate_path_lite
from google.genai import types

def write_file(working_dir, directory, content):
    try:
        working_path, target = validate_path_lite(working_dir, directory)

        if os.path.isdir(target):
            return f"Error: {target} is a directory and cant be written to"

        os.makedirs(os.path.dirname(target), exist_ok=True)
        
        with open(target, "w") as file:
            file.write(content)

        return f"Successfully wrote to \"{target}\" ({len(content)} characters written)"

    except Exception as e:
        return f"Failed to Write! - {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to the file (relative to project root), if the file or path does not exist, the relevant directories will be created (relative to project root)", 
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to write/overwire the specified file"
                ),
            },
        required=["directory", "content"]
        ),
    )
