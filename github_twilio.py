from github import Github
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIOSID")
auth_token = os.environ.get("TWILIOTOKEN")
g = Github(os.environ["GHUB"])

client = Client(account_sid, auth_token)
usr = g.get_user()
noti = [(a.repository.full_name, a.subject.title) for a in usr.get_notifications()]

def send_notification(notification):
    
    message = client.messages \
    .create(
        body = "GitHub Notification: {}".format(notification),
        from_= os.environ["TWILIOPHONE"],
        to = os.environ["MYPHONE"]
    )
    
    print(message.sid)
    
    return(True)

_ = [send_notification(notification) for notification in noti]
