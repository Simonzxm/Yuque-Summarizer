import json
import re
import requests

with open("config.json", "r") as f:
    config = json.load(f)
    key = config["yuque_api_key"]

headers = {"X-Auth-Token": key}

def format_url(url):
    """Get the API URL of given URL"""

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    match = re.match(r"^(https?://)([^/]+)/([^/]+)/([^/]+)/([^/]+)$", url)
    if match:
        scheme, netloc, group_login, book_slug, doc_slug = match.groups()
        new_path = f"/api/v2/repos/{group_login}/{book_slug}/docs/{doc_slug}"
        formatted_url = f"{scheme}{netloc}{new_path}"
        return {"url": formatted_url, "type": "doc"}
    
    match = re.match(r"^(https?://)([^/]+)/([^/]+)/([^/]+)$", url)
    if match:
        scheme, netloc, group_login, book_slug = match.groups()
        new_path = f"/api/v2/repos/{group_login}/{book_slug}/docs"
        formatted_url = f"{scheme}{netloc}{new_path}"
        return {"url": formatted_url, "type": "repo"}

def get_doc(url):
    """Get the Yuque content of the URL"""

    response = requests.get(url, headers = headers)
    doc = response.json()
    return doc["data"]

def get_doc_urls(url):
    """Get the doc urls under the repo of the URL"""

    response = requests.get(url, headers = headers)
    doc = response.json()
    count = doc["meta"]["total"]
    print(f"{count} docs under this repo..")
    urls = []
    for i in range(count):
        urls.append(url + "/" + doc["data"][i]["slug"])
    return urls


