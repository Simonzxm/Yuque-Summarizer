import openrouter
import yuque

url = input("Enter the URL:\n")
formatted_url = yuque.format_url(url)
text = yuque.get(formatted_url)
summary = openrouter.summarize(text)

with open("output.md", "w") as file:
    file.write(summary)
