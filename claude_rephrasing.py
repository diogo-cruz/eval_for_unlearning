import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()


def main():
  client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
  message = "Tell me a short joke about programming."
  try:
    response = client.messages.create(
      model="claude-3-opus-20240229",
      max_tokens=1000,
      messages=[
        {"role": "user", "content": message}
      ]
    )
    print("\nClaude's response:")
    print(response.content[0].text)
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 