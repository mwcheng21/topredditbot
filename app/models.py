from datetime import datetime
from app import db 


class User(db.Model) :
    sno = db.Column(db.Integer , primary_key = True)
    time = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable = False)
    subreddit = db.Column(db.String(60) , nullable = False)

    def get_id(self):
        try:
            return (self.sno)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __repr__(self):
        return  'User(%s , %s)' % (self.sno , self.phone)

