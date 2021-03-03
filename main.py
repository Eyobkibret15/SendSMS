from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACcefabb392661ef869a9ca3745f3fe637'
auth_token = 'dc9e2f84b18907c2c8fd6e61907a97bb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like eyob kibret.",
                     from_='+15022731170', # this one is twilio number
                     to='+48739621422'   # this my real phone number
                 )


print(message.sid)
