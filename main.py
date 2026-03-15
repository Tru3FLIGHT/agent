import os
from google import genai
from dotenv import load_dotenv

MODEL = "gemini-2.5-flash"

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("api key not found")
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model=MODEL, contents="in as few words as possible, tell me if you recived this api request")
    
    if response.usage_metadata == None:
        raise RuntimeError("Possible api error - no usage metadata")

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}\n=====\n{response.text}")
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        quit(1)
