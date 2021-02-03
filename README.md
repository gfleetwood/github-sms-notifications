# GitHub SMS Notifications

## Overview

A simple script to text you the repo's name and subject title when you have unread GitHub notifications. It runs on Heroku with a scheduler addon to check for notifications every couple of hours.

Here's a reproducibility checklist:

* Accounts with GitHub, Twilio, and Heroku and API keys for the first two. 

* The Heroku CLI installed

* A Twilio phone number

* Installation of the packages listed in requirements.txt.

* Environment variables "TWILIOPHONE", "MYPHONE", "TWILIOSID", "TWILIOTOKEN", "GHUB" where the last three are the aforementioned API keys. The phone numbers are strings of the form "+11231231234".

Steps:

* Clone this repo and run the script locally for testing. 

* Deploy it to Heroku

* Setup the environment variables in the Heroku dashboard.

* Follow [this](https://medium.com/analytics-vidhya/schedule-a-python-script-on-heroku-a978b2f91ca8) tutorial to setup the scheduler addon.

In retrospect it would have been neater to set up the scheduler as a GitHub Action. Maybe next time.
