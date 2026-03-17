from functions import get_files_info
from functions import get_file_content
from functions import run_python_file
from functions import get_files_info
from functions import write_file
from functions import get_file_content
from google.genai import types

available_functions = types.Tool(
        function_declarations=[get_files_info.schema_get_files_info, get_file_content.schema_get_file_content],
        )
