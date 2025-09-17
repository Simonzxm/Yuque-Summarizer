import json
from openai import AsyncOpenAI

with open("config.json", "r") as f:
    config = json.load(f)
    client = AsyncOpenAI(
        base_url = config["llm_base_url"],
        api_key = config["llm_api_key"]
    )
    model = config["llm_model"]

async def summarize(title, body):
    """Summarize the html"""
    
    completion = await client.chat.completions.create(
        extra_headers = {},
        extra_body = {},
        model = model,
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Summarize the html below and reply only the summary in Chinese. Title: {title}, Body: {body}"
                    }
                ]
            }
        ]
    )
    return completion.choices[0].message.content
