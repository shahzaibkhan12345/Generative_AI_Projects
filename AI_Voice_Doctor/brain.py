#Step 1: Setup Groq API key
import os
groq_api_key= os.getenv("GROQ_API_KEY")
#step 2: Convert Image to Required Format

import base64

def encode_image(image_path):
    #image_path = "Acne.jpg" 
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step 3:Setup Multimodl LLM
from groq import Groq

query="Is there any wrong with my Face?"
model="meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_image_with_query(query,model,encode_image):
    client = Groq(api_key=groq_api_key)
    completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image}"
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

    return completion.choices[0].message.content

