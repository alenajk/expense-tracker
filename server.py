import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from twilio.rest import TwilioRestClient
import twilio.twiml

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

# Source twilio credentials
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid:
    print "Source your secrets!"

client = TwilioRestClient(account_sid, auth_token)

class Expense(db.Model):
	expenseid = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
	amount = db.Column(db.Float)
	category = db.Column(db.String(80))
	description = db.Column(db.String(80))

@app.route("/")
def hello():

	print db.session.query(Expense).all()
	msgs = [str(msg.body) for msg in client.messages.list()]

	return render_template('homepage.html', msgs=msgs)

@app.route("/newmsg", methods=['GET','POST'])
def savemsg():

	if request.method == "POST":
		msg = request.form.get('Body')
		print 'msg :', msg

	return 'Testing newmsg app route'

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)