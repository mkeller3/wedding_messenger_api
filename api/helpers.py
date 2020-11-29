import string
import random
from twilio.rest import Client
import os

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

def sendTextMessage(to,body,mediaUrl=False):
    if mediaUrl:
        message = client.messages.create(
            body=body,
            from_='+13312041678',
            media_url=[mediaUrl],
            to='+1'+str(to)
        )
    else:
        message = client.messages.create(
            body=body,
            from_='+13312041678',
            to='+1'+str(to)
        )

def id_generator(size=50, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))