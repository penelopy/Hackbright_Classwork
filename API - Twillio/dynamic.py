from flask import Flask, request
from twilio.rest import TwilioRestClient
import twilio.twiml

# Pull in configuration from system environment variables
TWILIO_ACCOUNT_SID = 'ACb6a98af4175efef31a85487959be87c2'
TWILIO_AUTH_TOKEN = '0bc3b9021a96b48fe331e8df748a0354'
TWILIO_NUMBER = '+19717035852'

app = Flask(__name__)

callers = {
	"+16509964810": "Gowri",
	"+14155290299": "Wendy",
	"+19162233386": "Danielle",
	"+14155132470": "Joel"
}

@app.route("/", methods=['GET', 'POST'])
def hello_custom():
	from_number = request.values.get('From')
	if from_number in callers:
		name = callers[from_number]
	else: 
		name = "Hacker"

	message = "Hello, {}, thanks for the message!".format(name)
	resp = twilio.twiml.Response()

	resp.message(message)
	return str(resp)

if __name__=="__main__": 
	app.run(debug=True)