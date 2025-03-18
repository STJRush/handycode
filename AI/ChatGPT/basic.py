from openai import OpenAI
import secrets  # Import the secrets file

# Use the API key stored in secrets.py
client = OpenAI(api_key=secrets.OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)
