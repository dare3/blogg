# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.text(50), nullable=False)
    last_name = db.Column(db.text(50), nullable=False)
    image_url = db.Column(db.text, nullable=False, default='https://facecard.com')

    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.text(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Post {self.title} by User {self.user_id}>'


# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.Text, nullable=False)
#     last_name = db.Column(db.Text, nullable=False)
#     image_url = db.Column(db.Text, nullable=False)  # Adjust the length as needed

# def connect_db(app):

#     db.app = app
#     db.init_app(app)

#     def __repr__(self):
#         return f"<User {self.id}: {self.first_name} {self.last_name}>"

# from flask_sqlalchemy import SQLAlchemy