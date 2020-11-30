from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# def get_token():

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes= scopes)
credentials = flow.run_local_server(port=0)
pickle.dump(credentials, open("token.pkl", "wb"))
creds = pickle.load(open("token.pkl", "rb"))

service = build('calendar', 'v3', credentials=creds)

    # return service