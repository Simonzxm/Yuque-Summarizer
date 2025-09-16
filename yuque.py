import re
import requests

with open("yuque.key", "r") as f:
    key = f.read()

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
        return formatted_url

def get(url):
    """Get the Yuque content of the URL"""
    response = requests.get(url, headers = headers)
    doc = response.json()
    return doc["data"]["body"]
