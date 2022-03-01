import requests as rq
from html import unescape

params = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = rq.get("https://opentdb.com/api.php", params=params)

question_data = response.json()["results"]

for question in question_data:
    question["question"] = unescape(question["question"])
