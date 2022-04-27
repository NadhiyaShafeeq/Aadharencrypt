from twilio.rest import Client
import os


def sendMessageToPhone(encrypted_data):
    account_sid = "ACe4a307c82d337b43529f09314b41f533"
    auth_token = "6d281728e4111bddc479baa55752c1ee"
    # account_sid = os.getenv('ACCOUNT_SID')
    # auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your login credentials are: http://test.com/token={encrypted_data}",
        from_="+19704632807",
        to="+917994244793"
    )
    return message.sid
