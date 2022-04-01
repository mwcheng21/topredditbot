from sre_constants import SUCCESS
from flask import render_template, request
from app import app, db
from app.models import User



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
        return render_template("index.html", added=1)

    return render_template("index.html", added=0)
