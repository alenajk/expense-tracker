import os
from datetime import datetime
from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient
import twilio.twiml
from model import Expense, connect_to_db, db

app = Flask(__name__)

# Source secrets
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid:
    print "Source your secrets!"

client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET','POST'])
def hello():

    msgs = [msg for msg in db.session.query(Expense).all()]

    for msg in msgs:
        msg.date = msg.date.isoformat()
        msg.description = str(msg.description)
        msg.amount = "$" + str(msg.amount)
        if msg.amount[-2:] == ".0":
            msg.amount = msg.amount[:-2]

    categories = set([str(msg.category) for msg in msgs])
    if request.method == "POST":
        for msg in msgs:
            if msg.category not in request.form.getlist('category'):
                msgs.remove(msg)

    return render_template('homepage.html', msgs=msgs,categories=categories)

@app.route("/newmsg", methods=['GET','POST'])
def savemsg():

    if request.method == "POST":
        msg = request.form.get('Body')
        date = str(datetime.now()).split()[0]
        msg_parsed = msg.split()
        amount = msg_parsed[0]
        category = msg_parsed[1]
        description = ' '.join(msg_parsed[2:])
        expense = Expense(date=date,amount=amount,category=category,description=description)
        db.session.add(expense)
        db.session.commit()

    return 'Testing newmsg app route'

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))
    connect_to_db(app)
    app.run(host='0.0.0.0', port=port)