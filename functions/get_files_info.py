import os
from functions.path_validation import validate_path
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        working_dir_path, target_dir = validate_path(working_directory, directory)
        ls = "Result for current directory:\n"
        for dir in os.listdir(target_dir):
            dirpath = os.path.join(target_dir, dir)
            name = dir
            byte = os.path.getsize(dirpath)
            is_dir = os.path.isdir(dirpath)
            ls = ls + f"    - {name}: file_size: {byte} bytes, is_dir={is_dir}\n"
        return ls


    except Exception as e:
        return e

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)", 
                ),
            },
        required=["directory"]
        ),
    )
