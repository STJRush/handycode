from openai import OpenAI
import mysecrets
import base64

# Load the image file and encode it in base64
image_path = "food.jpg"

with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Initialize OpenAI client with API key
client = OpenAI(api_key=mysecrets.API_KEY)

# Send image to OpenAI for analysis
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                },
            },
        ],
    }],
)

# Print the result
print(response.choices[0].message.content)

