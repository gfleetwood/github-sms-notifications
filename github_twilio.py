from os import environ
from github import Github
from twilio.rest import Client

def send_sms(notification):
    
    message = client.messages \
    .create(
        body = "GitHub Notification: {}".format(notification),
        from_ = from_phone,
        to = to_phone
    )
    
    return(True)

from_phone = environ["TWILIOPHONE"]
to_phone = environ["MYPHONE"]
twilio_sid = environ["TWILIOSID"]
twilio_token = environ["TWILIOTOKEN"]
client = Client(twilio_sid, twilio_token)

g = Github(os.environ["GHUB"])
usr = g.get_user()
notifications = [(notification.repository.full_name, notification.subject.title) for notification in usr.get_notifications()]

_ = send_sms("No notifications") \
    if len(notifications) == 0 \
    else [send_sms(notification) for notification in notifications]
