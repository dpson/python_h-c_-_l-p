from twilio.rest import TwilioRestClient
### your account sid an auth token from twilio.com/user/account
account_sid = "ACc0aa18c224fa2d295957d2dbd5c0ceaa"
auth_token = "4a0f9c6bf82500bb816b04738f00e7b5"

client = TwilioRestClient(account_sid,auth_token)
while True:
    number = input("number: ")
    message = client.messages.create(body= "toi nay anh nhe",to="+84%s"%number,from_= "+12015286688")
    print(message.sid)
