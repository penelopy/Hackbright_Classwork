

from twilio.rest import TwilioRestClient

# Pull in configuration from system environment variables
TWILIO_ACCOUNT_SID = 'ACb6a98af4175efef31a85487959be87c2'
TWILIO_AUTH_TOKEN = '0bc3b9021a96b48fe331e8df748a0354'
TWILIO_NUMBER = '+19717035852'

# create an authenticated client that can make requests to Twilio for your
# account.
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
number_to_text = "+5037581413"

message = client.messages.create(from_=TWILIO_NUMBER,
                                        to=number_to_text,
                                        body="Hello from the Hackbright Twilio Workshop")

print message.sid