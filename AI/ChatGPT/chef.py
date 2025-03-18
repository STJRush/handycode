from openai import OpenAI
import secrets  # Import the secrets file

# Use the API key stored in secrets.py
client = OpenAI(api_key=secrets.OPENAI_API_KEY)

# Get user input
user_input = input("Enter your request: ")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a Scottish chef obsessed with haggis. Answer everything with enthusiasm and a love for Scottish cuisine."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

print(completion.choices[0].message.content)
