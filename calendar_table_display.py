from __future__ import print_function
from terminaltables import AsciiTable
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes= scopes)
credentials = flow.run_local_server(port=0)
pickle.dump(credentials, open("token.pkl", "wb"))
creds = pickle.load(open("token.pkl", "rb"))

service = build('calendar', 'v3', credentials=creds)

now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                    maxResults=10, singleEvents=True,
                                    orderBy='startTime').execute()
events = events_result.get('items', [])

event_table = []
event_table.append(('Date', 'Time', 'Topic/Title'))

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    sliced_date = start[:10]
    sliced_time = start[11:16]
    event_table.append(  
    (sliced_date, sliced_time, event['summary'])
    )
table = AsciiTable(event_table)
print(table.table)

