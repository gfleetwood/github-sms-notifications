import os
from github import Github
from twilio.rest import Client

def send_sms(notification):
    
    message = client.messages \
    .create(
        body = "GitHub Notification: {}".format(notification),
        from_= os.environ["TWILIOPHONE"],
        to = os.environ["MYPHONE"]
    )
    
    return(True)

account_sid = os.environ.get("TWILIOSID")
auth_token = os.environ.get("TWILIOTOKEN")
client = Client(account_sid, auth_token)

g = Github(os.environ["GHUB"])
usr = g.get_user()

notifications = [(a.repository.full_name, a.subject.title) for a in usr.get_notifications()]

_ = send_sms("No notifications") \
    if len(notifications) == 0 \
    else [send_sms(notification) for notification in notifications]
