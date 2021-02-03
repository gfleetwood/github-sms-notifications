from github import Github
import os
from twilio.rest import Client

def send_notification(notification):
    
    message = client.messages \
    .create(
        body = "GitHub Notification: {}".format(notification),
        from_= os.environ["TWILIOPHONE"],
        to = os.environ["MYPHONE"]
    )
    
    return(True)

account_sid = os.environ.get("TWILIOSID")
auth_token = os.environ.get("TWILIOTOKEN")
g = Github(os.environ["GHUB"])
client = Client(account_sid, auth_token)
usr = g.get_user()

noti = [(a.repository.full_name, a.subject.title) for a in usr.get_notifications()]
_ = send_notification("No notifications") if len(noti) == 0 else [send_notification(notification) for notification in noti]
