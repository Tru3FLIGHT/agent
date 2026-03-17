import os
from functions.path_validation import validate_path
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_dir, directory='.'):
    try:
        working_dir_path, target_dir = validate_path(working_dir, directory)
        
        if not os.path.isfile(target_dir):
            return f"Error: {target_dir} is not a file... is_file={os.path.isfile(target_dir)} is_dir={os.path.isdir(target_dir)}"
        with open(target_dir, "r") as file:
            content = file.read(MAX_CHARS)
            if file.read(1):
                content += f"\n[file \"{target_dir}\" was truncated at {MAX_CHARS} characters]"
        return content

    except Exception as e:
        return e

schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads a specified file relative to the working directory, providing the contents",
        parameters=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to be read, relative to the working directory",
                ),
            },
        ),
)
