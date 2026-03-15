import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_path, directory))
        if not os.path.exists(target_dir):
            return f'Error: "{directory}" is not a directory'
        #bool
        valid_target_dir = os.path.commonpath([working_dir_path, target_dir]) == working_dir_path
        if not valid_target_dir:
            return f"Error: cannot list \"{directory}\" as it is outside the permitted working directory"
        
    except Exception as e:
        return e
