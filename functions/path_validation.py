import os

def validate_path(working_directory, directory='.'):
    working_dir_path = os.path.abspath(working_directory)
            
    if directory == ".":
        target_dir = working_dir_path
    else:
        target_dir = os.path.normpath(os.path.join(working_dir_path, directory))
    if not os.path.exists(target_dir):
        raise Exception(f'Error: "{directory}" is not a directory')
    #bool
    valid_target_dir = os.path.commonpath([working_dir_path, target_dir]) == working_dir_path
    if not valid_target_dir:
        raise Exception(f"Error: cannot access \"{directory}\" as it is outside the permitted working directory")
    return working_dir_path, target_dir
