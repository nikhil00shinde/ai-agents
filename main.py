import os
import argparse
from google import genai
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=args.user_prompt
    )

    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    # print(response.text)
    # print(response.usage_metadata)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
