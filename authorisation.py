from __future__ import print_function
import os
import pickle
import getpass
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
from googleapiclient.discovery import build
#we'll add deregister to delete the token

creds = None
SCOPES = ['https://www.googleapis.com/auth/calendar']

def token_exists():
    """checks if the token file exists or not"""

    if os.path.exists('token.pickle'):
        return True
    return False


def get_creds():
    """gets credentials from the token"""
    global creds

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    return creds


def token_valid():
    """Checks if the token is valid(not expired)"""

    if os.path.exists('token.pickle') and creds and creds.valid:
        return True
    return False


def read_json(filename='.secret.json'):
    with open(filename,'r') as json_file: 
        data = json.load(json_file)
    return data


def write_json(data, filename='.secret.json'):
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)


def register_user():
    """Creates a new user"""

    print("Please enter your username and password to register")
    user = getpass.getuser()
    print(f'Username: {user}')
    password = getpass.getpass(prompt='Password: ')
    pass_comfirm = getpass.getpass(prompt='Confirm password: ')

    if password == pass_comfirm:
        print(f"Welcome to Code Clinic {user}")
        data = read_json(filename='.secret.json')
        user_details = {
        "user_name" : user,
        "password" : password   
        }
        temp = data['user_infomation']
        temp.append(user_details)
        write = write_json(data, filename='.secret.json')


        flow = InstalledAppFlow.from_client_secrets_file(
                    '.secret.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

    else:
        print("ERROR! Passwords don't match")
        return password
   

def get_user():
    return getpass.getuser()


def get_event():
    service,now = build_calendar()

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def build_calendar():
    """Build the calendar"""
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    return service, now


def user_login():
    """"logs in an existing user"""

    global creds

    print("Please enter your username and password to login")
    user = getpass.getuser()
    print(f'Username: {user}')
    password = getpass.getpass(prompt='Password: ')
    
    with open('.secret.json') as json_file:
        json_object = json.load(json_file)
        
    user_details = {
        "user_name" : user,
        "password" : password   
        }

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if user_details in json_object["user_infomation"]:
        print("Sucessful Login")
    else:
        print("Incorrect username or password")

creds = get_creds()
