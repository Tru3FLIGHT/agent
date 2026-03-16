import os
from functions.path_validation import validate_path

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
