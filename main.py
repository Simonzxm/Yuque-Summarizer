import aiohttp
import asyncio
import llm
import yuque

async def process_doc(session, doc_url):
    """Return title and summary of given doc"""
    doc = await yuque.get_doc(session, doc_url)
    summary = await llm.summarize(doc["title"], doc["body"])
    return {"title": doc["title"], "summary": summary}

async def main():
    url = input("Enter the URL:\n")
    formatted_url = yuque.format_url(url)
    output = ""

    async with aiohttp.ClientSession() as session:

        if formatted_url["type"] == "doc":
            doc = await yuque.get_doc(session, formatted_url["url"])
            summary = await llm.summarize(doc["title"], doc["body"])
            title = doc["title"]
            output = f"|Title|\n|-|\n|{title}|\n\n{summary}"

        elif formatted_url["type"] == "repo":
            doc_urls = await yuque.get_doc_urls(session, formatted_url["url"])
            tasks = [process_doc(session, doc_url) for doc_url in doc_urls]
            results = await asyncio.gather(*tasks)
            for result in results:
                output += f"|Title|\n|-|\n|{result['title']}|\n\n{result['summary']}\n\n"

    with open("output.md", "w", encoding="utf-8") as f:
        f.write(output)
        print("Summary written to output.md!")

if __name__ == "__main__":
    asyncio.run(main())