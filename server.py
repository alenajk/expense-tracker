import os
from flask import Flask, render_template
from twilio.rest import TwilioRestClient
app = Flask(__name__)

# Source twilio credentials
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

if not account_sid:
    print "Source your secrets!"

client = TwilioRestClient(account_sid, auth_token)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)