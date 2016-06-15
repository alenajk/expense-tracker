import os
from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient
import twilio.twiml
app = Flask(__name__)

# Source twilio credentials
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid:
    print "Source your secrets!"

client = TwilioRestClient(account_sid, auth_token)

@app.route("/")
def hello():
    msgs = [str(msg.body) for msg in client.messages.list()]
    print msgs, type(msgs), msgs[1]
    print dir(client.messages)
    return render_template('homepage.html', msgs=msgs)

@app.route("/newmsg", methods=['GET','POST'])
def savemsg():
	print "testing"
	if request.method == "POST":
		msg = request.form.get('Body')
		print 'request.body :', request.body
		print 'msg :', msg

	return 'Testing newmsg app route'

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)