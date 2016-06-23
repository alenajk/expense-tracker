from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class Expense(db.Model):
    expenseid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Float)
    category = db.Column(db.String(80))
    description = db.Column(db.String(80))

def connect_to_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB"