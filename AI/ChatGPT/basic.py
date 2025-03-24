# Uuse pip install --upgrade openai to ensure you have the latest version of the openai package.
# The OpenAI class is now available in the openai package, which simplifies the process of making API requests.
# Find the documentation for the OpenAI class here: https://platform.openai.com/docs/guides/text?api-mode=chat&lang=python


rom secrets import API_KEY
from openai import OpenAI

# Ensure your openai package is updated to the version that supports the OpenAI class.
client = OpenAI(api_key=API_KEY)

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
