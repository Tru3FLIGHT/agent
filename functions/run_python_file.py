import os
import subprocess
from functions.path_validation import validate_path

def run_python_file(working_dir, directory, args=None):
    try:
        wdp, target = validate_path(working_dir, directory)

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
