import os
from functions.path_validation import validate_path

def get_file_content(working_dir, directory='.'):
    try:
        working_dir_path, target_dir = validate_path(working_dir, directory)
    except Exception as e:
        return e
