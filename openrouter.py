from openai import OpenAI

with open("openrouter.key", "r") as f:
    key = f.read()

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = key,
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
