from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import send
import time
import threading
import os

# # to update sqllite db
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/site.db'
# db = SQLAlchemy(app)

#then run 
# from app import db
# db.create_all()
def checker():
    hr = 0
    time.sleep(0)
    while True:
        send.sendTexts(hr)
        hr += 1
        time.sleep(360)

if __name__ == "__main__" :
    app.secret_key = "secret key"

    x = threading.Thread(target=checker)
    x.start()
    app.run(debug = True, use_reloader=False)
