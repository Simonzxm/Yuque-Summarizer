import json
from openai import OpenAI

with open("config.json", "r") as f:
    config = json.load(f)
    client = OpenAI(
        base_url = config["llm_base_url"],
        api_key = config["llm_api_key"]
    )

def summarize(text):
    """Summarize the html"""
    
    completion = client.chat.completions.create(
        extra_headers = {},
        extra_body = {},
        model = "openrouter/sonoma-sky-alpha",
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Summarize the html below and reply only the summary in Chinese:" + text
                    }
                ]
            }
        ]
    )
    return completion.choices[0].message.content
