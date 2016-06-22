import os
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
    connect_to_db(app)
    app.run(host='0.0.0.0', port=port)