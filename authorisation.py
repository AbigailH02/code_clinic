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
import time
from unittest import mock
#we'll add deregister to delete the token

creds = None
SCOPES = ['https://www.googleapis.com/auth/calendar']

def token_exists():
    """checks if the token file exists or not"""

    if os.path.exists('token.pickle'):
        # print('token_exists')
        return True
    return False


def creds_expired():
    global creds
    
    if creds.expired:
        print("creds expired")
        return True
    return False



def get_creds():
    """gets credentials from the token"""
    global creds

    if os.path.exists('token.pickle') and not token_expired():
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # elif token_exists() and token_expired():
    #     creds.refresh(Request())
    return creds


def token_valid():
    """Checks if the token is valid(not expired)"""

    if os.path.exists('token.pickle') and creds and creds.valid:
        # print('Token is valid')
        return True
    return False

def token_expired():
    """gets the date and time of token file
        token expires after one hour
        if the expiry date of the token is greater than the current time
        it is expired"""

    created = os.path.getctime("token.pickle")
    
    token_exp = created + 3600
    now = time.time()

    if token_exp < now:
        # print('token expired')
        return True
    else:
        # print(f"\n\ttoken will expire on {time.ctime(token_exp)}")#token expires after 3600seconds(1hour)
        return False


def register_user():
    """Creates a new user"""

    print("Please enter your username and password to register")
    user = getpass.getuser()
    print(f'Username: {user}')
    password = getpass.getpass(prompt='Password: ')
    pass_comfirm = getpass.getpass(prompt='Confirm password: ')

    if password == pass_comfirm:
        print(f"Welcome to Code Clinic {user}")
        with open('secret.json') as json_file:
            data = json.load(json_file)
        user_details = {
        "user_name" : user,
        "password" : password   
        }

        json_object = json.dumps(user_details, indent = 4)
        with open('secret.json','w') as f: 
            f.write(json_object)
        # temp = data['user_infomation']
        # temp = user_details

        # with open('secret.json','w') as f: 
        #     json.dump(data, f, indent=4)

        flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

    else:
        print("ERROR! Passwords don't match")
   
    

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
    creds = get_creds()

    print("Please enter your username and password to login")
    user = getpass.getuser()
    print(f'Username: {user}')
    password = getpass.getpass(prompt='Password: ')

    with open('secret.json') as json_file:
        json_object = json.load(json_file)
        
    user_details = {
        "user_name" : user,
        "password" : password   
    }

    if token_exists() and creds.expired:
        print("Refreshing the login token...")
        creds.refresh(Request())
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
   
    if user_details == json_object:
        print("Sucessful Login")
    else:
        print("Incorrect username or password")


creds = get_creds()
# user_login()
# (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('token.pickle')
# print("\ttoken Created: %s" % time.ctime(ctime))
# print(f"\tmodified time: {time.ctime(mtime)}")
