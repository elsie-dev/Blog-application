from datetime import datetime
from db import db

# class Books(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     author = db.Column(db.String)


#     def to_json(self):
#         return {'id': self.id, 'title': self.title, 'author': self.author}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    user_name = db.Column(db.String(100))
    password =db.Column(db.String(60), nullable=False)
    acount_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    acount_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_json(self):
        return {'id': self.id,'first_name':self.first_name,'last_name':self.last_name,'user_name':self.user_name,'image_url':self.image_url,'acount_created':self.acount_create,'acount_updated':self.acount_updated}




class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100))
    url = db.Column(db.String(100))
    upload_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_json(self):
        return {'id': self.id,'file_name':self.file_name,'url':self.url,'user_id':self.user_id,'upload_date':upload_date}
