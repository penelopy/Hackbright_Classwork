from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	#Respond to incoming text message with a static response
	resp = twilio.twiml.Response()
	resp.message("Hello, Hackbright Monkey")
	return str(resp)

if __name__=="__main__":
	app.run(debug=True)