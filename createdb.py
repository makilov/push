from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # Import datetime module

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workouts = db.relationship('Workout', backref='author', lazy=True)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create a function to initialize the database tables
def init_db():
    with app.app_context():
        db.create_all()

# Call the init_db function to create the database tables
init_db()

if __name__ == '__main__':
    app.run(debug=True)
