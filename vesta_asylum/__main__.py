import requests
import json
from loguru import logger

from . import ENV

logger.add(sink="main.log", level="INFO")

HEADERS = {
    "Content-Type": "application/json",
    "X-Vestaboard-Read-Write-Key": ENV["API_KEY"]
}

def get_message():
    url = "https://rw.vestaboard.com/"

    response = requests.get(url, headers=HEADERS)

    print(response.text)
    return response.status_code

def post_message():
    url = "https://rw.vestaboard.com/"
    data = {
        "text": "Hello World 2"
    }

    response = requests.post(url, headers=HEADERS, data=json.dumps(data))

    print(response.text)
    return response.status_code

if __name__ == "__main__":
    get_message()
    post_message()