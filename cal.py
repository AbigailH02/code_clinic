from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

event_dict = {}

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    return service, now
   

def get_event(service,now):
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def create_event(title, date, time):        
    event = {}
    duration=30
    time = datetime.time(int(time.split(':')[0]),int(time.split(':')[1]))
    full_date = datetime.datetime(1,1,1,time.hour,time.minute)
    new_date = datetime.timedelta(minutes=30) + full_date
    end = f'{date}T{new_date.time()}+02:00'
    start = f'{date}T{time}+02:00'
    
    event.update({'summary':title})
    event.update({'start':{'dateTime':start}})
    event.update({'end':{'dateTime':end}})
    return event
    
def insert_event(service, event):
    event = service.events().insert(calendarId='primary', body=event).execute()
    event_dict.update({event['summary']:event})


def write_data(slots_dict, file):
    with open(file,'w') as f: json.dump(slots_dict,f)


if __name__ == '__main__':
    pass
    # service, now = main()
    # get_event(service,now)
    # event = create_event('metting','2020-11-12','17:00')
    # insert_event(service, event)


# from __future__ import print_function
# import datetime
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# # from google.auth.transport.requests import Request
# from google.auth.transport.requests import Request
# import json

# event_dict = {}

# def init_api():
#     # If modifying these scopes, delete the file token.pickle.
#     SCOPES = ['https://www.googleapis.com/auth/calendar']

#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('calendar', 'v3', credentials=creds)
#     return service


# def read_data(file):
#     with open(file) as f: return json.load(f)


# def write_data(slots_dict, file):
#     with open(file,'w') as f: json.dump(slots_dict,f)


# def create_event(title, date, time):        
#     event = {}
#     duration=30
#     time = datetime.time(int(time.split(':')[0]),int(time.split(':')[1]))
#     full_date = datetime.datetime(1,1,1,time.hour,time.minute)
#     new_date = datetime.timedelta(minutes=30) + full_date
#     end = f'{date}T{new_date.time()}+02:00'
#     start = f'{date}T{time}+02:00'
    
#     event.update({'summary':title})
#     event.update({'start':{'dateTime':start}})
#     event.update({'end':{'dateTime':end}})
#     return event
    

# def insert_event(service, event):
#     event = service.events().insert(calendarId='primary', body=event).execute()
#     event_dict.update({event['summary']:event})


# def delete_event(service, event):
#     event_id = event['id']
#     service.events().delete(calendarId='primary', eventId=event_id).execute()
#     event_dict.pop(event['summary'])


# def add_email_event(service, event, email):
#     summary = event['summary']
#     start = event['start']
#     end = event['end']
#     delete_event(service, event)
#     event = {}     
#     event.update({'summary':summary})
#     event.update({'start':start})
#     event.update({'end':end})
#     event.update({'attendee':[]})
#     event['attendee'].append({'email':email})
#     insert_event(service, event)

# service = init_api()
# # print(service)

# print(create_event('meet','2020-12-12',"17:00"))