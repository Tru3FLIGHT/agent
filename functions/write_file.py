import os
from functions.path_validation import validate_path_lite

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
