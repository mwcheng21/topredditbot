# Run python3 ./main.py [TIME]
import os
from twilio.rest import Client
import requests
import json 
import sqlite3
import sys


def sendText(user):
    print(1)
    subreddit = user[3]
    to=user[2]
    url = "https://www.reddit.com/r/{{subreddit}}/top.json?limit=1".replace("{{subreddit}}", subreddit)
    html = requests.get(url,  headers = {'User-agent': 'reddit-bot'})
    text = json.loads(html.text)

    title = text["data"]["children"][0]["data"]["title"]
    body = text["data"]["children"][0]["data"]["selftext"]
    src = text["data"]["children"][0]["data"]["url"]

    message = "\n" + title + "\n" + body + "\n" + src
    account_sid = "sid"
    auth_token = "auth"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_='+13203481536',
                        to=to
                    )


def sendTexts(thisTime):
    conn = sqlite3.connect("app/site.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        if str(row[1]) == str(thisTime):
            sendText(row)