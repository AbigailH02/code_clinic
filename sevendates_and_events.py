from __future__ import print_function
from terminaltables import AsciiTable
import datetime
from datetime import date
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

later = []
# credentials = 'client_secret.json'

# # scopes = ['https://www.googleapis.com/auth/calendar']
# # flow = InstalledAppFlow.from_client_secrets_file(credentials, scopes= scopes)
# # credentials = flow.run_local_server(port=0)
# # pickle.dump(credentials, open("token.pkl", "wb"))
# creds = pickle.load(open("token.pkl", "rb"))

# service = build('calendar', 'v3', credentials=creds)

def getting_dates():
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    current = datetime.datetime.today()

    for x in range(0, 7):
        y = (current + datetime.timedelta(days=x))
        y = y.isoformat() + 'Z'
        later.append(y)
    print(later)
    return now, later

def getting_events(now, later):
    page_token = None
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token, timeMin=now, timeMax=later[-1], singleEvents=True, orderBy="startTime").execute()
        list_events = []
        for event in events['items']:
            test_var = event['summary']
            list_events.append(test_var)
        print(list_events)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return list_events 


def run_prog():
    now, later = getting_dates()
    list_events = getting_events(now, later)
