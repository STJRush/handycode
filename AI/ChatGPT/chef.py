import openai
import config  # Import the config file containing the API key

# Set up the OpenAI API key using the variable from config.py
openai.api_key = config.OPENAI_API_KEY

# Get user input
user_input = input("Enter your request: ")

response = openai.ChatCompletion.create(
    model="gpt-4",
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

print(response["choices"][0]["message"]["content"])
