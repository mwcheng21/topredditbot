from sre_constants import SUCCESS
from flask import render_template, request
from app import app, db
from app.models import User
import send
import requests
import json
from twilio.rest import Client

def confirmation(number):
    account_sid = "ACb81379b8253073c0518cab2ce25633b8"
    auth_token = "cce237c9decd3d0aebfba69f7fd29a32"
    client = Client(account_sid, auth_token)
    message = "Welcome to DRP, your daily reddit post."
    message = client.messages \
                    .create(
                        body=message,
                        from_='+13203481536',
                        to=number
                    )


@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        sub = request.form["subreddit"]
        phone = request.form["phone"].replace("-", "")
        time = request.form["time"]
        if "r/" in request.form["subreddit"]:
            sub = sub[2:]
        user = User.query.filter_by(time=time, phone=phone, subreddit=sub).first()
        if user:
            return render_template("index.html", added=-1)
        element = User(time=time, phone=phone, subreddit=sub)
        db.session.add(element)
        db.session.commit()
        confirmation(phone)
        return render_template("index.html", added=1)

    return render_template("index.html", added=0)
