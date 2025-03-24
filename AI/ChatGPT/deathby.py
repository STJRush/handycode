from secrets import API_KEY
from openai import OpenAI

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are the magical abyss and some player has rolled a 1 on a d20 while asking for an item and therefore is annihilated in the form of 'Death by'. Whatever they ask for, you describe how it leads to their demise."
        },
        {
            "role": "user",
            "content": "Olives"
        }
    ]
)

print(completion.choices[0].message.content)
