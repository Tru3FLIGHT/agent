# Chatbot Project

This project implements a chatbot application powered by the Google Gemini API. The chatbot is designed to interact with users, process their prompts, and potentially execute various functions based on the Gemini model's output.

## Features

- **Gemini API Integration**: Leverages the Google Gemini API for natural language understanding and generation.
- **Function Calling**: Capable of calling predefined functions based on the model's interpretation of user prompts.
- **Interactive Conversations**: Engages in multi-turn conversations with users.
- **Verbose Mode**: Provides detailed output for debugging and understanding the chatbot's internal workings.

## How it Works

The `main.py` script is the entry point of the application. It parses user prompts, initializes the Gemini client, and manages the conversation flow. The chatbot iteratively sends user messages to the Gemini model and processes its responses. If the model suggests a function call, the application executes that function and incorporates the results back into the conversation.

## Setup and Usage

(Further setup and usage instructions would go here, e.g., how to set up the Gemini API key, install dependencies, and run the script.)

## File Structure

```
.
├── .git/                     # Git version control directory
├── .gitignore                # Specifies intentionally untracked files to ignore
├── .python-version           # Specifies the Python version used by the project
├── .venv/                    # Python virtual environment
├── .env                      # Environment variables for the project
├── __pycache__/              # Python cache directory
├── uv.lock                   # Lock file for uv package manager
├── pyproject.toml            # Project configuration for Python tools
├── README.md                 # This README file
├── main.py                   # Main application entry point and conversational logic
├── call_function.py          # Handles the execution of tool functions
├── prompts.py                # Defines prompts and conversational templates
├── calculator/               # Directory containing calculator tool functions
│   └── ...
├── functions/                # Directory containing other tool functions
│   └── ...
├── test_get_files_info.py    # Unit test for get_files_info function
├── test_get_file_content.py  # Unit test for get_file_content function
├── test_write_file.py        # Unit test for write_file function
└── test_run_python_file.py   # Unit test for run_python_file function
```
