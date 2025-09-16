import llm
import yuque

url = input("Enter the URL:\n")
formatted_url = yuque.format_url(url)
output = ""

if (formatted_url["type"] == "doc"):
    doc = yuque.get_doc(formatted_url["url"])
    summary = llm.summarize(doc["title"], doc["body"])
    title = doc["title"]
    output = f"Title: {title}\nSummary:\n{summary}"

elif (formatted_url["type"] == "repo"):
    urls = yuque.get_doc_urls(formatted_url["url"])
    for i in range(len(urls)):
        doc = yuque.get_doc(urls[i])
        summary = llm.summarize(doc["title"], doc["body"])
        title = doc["title"]
        output += f"Title: {title}\nSummary:\n{summary}\n\n\n"

with open("output.md", "w") as f:
    f.write(output)
    print("Summary written to output.md!")
