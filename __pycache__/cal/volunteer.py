import pickle, datetime, getpass
from googleapiclient.discovery import build

def create_event(summary, start, duration):

#
    event = {
        'summary':summary,
        'start': {
            'dateTime': start
        },
        'end':{
            'dateTime': duration
        },
        'attendees':{
            'email': f"{getpass.getuser()}@student.wethinkcode.co.za"
        }
    }
    print(event)
    return event 


def get_service():
    creds = None

    # NOTE: Remember to update the token to get creds
    # update_token()

    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def insert_event(service, event):
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event


def open_slots():
    service = get_service()
    summary = input(f"Please enter title of slot: [title]\n > ")
    date = input(f"Please choose date for opening slot: [yyyy-mm-dd]\n > ")
    time = input(f"Please choose time range for slots: [hh:mm]\n > ")
    slots = input(f"Please choose ammount of slots: [ammount]\n > ")

    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])
    hour = int(time.split(':')[0])
    minutes = int(time.split(':')[1])
    begin = datetime.datetime(year, month, day, hour, minutes)
    start = f"{begin.date()}T{begin.time()}+02:00"
    end = begin + datetime.timedelta(minutes=30)
    duration = f"{end.date()}T{end.time()}+02:00"

    #NOTE: Needs changes
    event_list = []

    for amm in range(int(slots)):
        event = insert_event(service, create_event(summary, start, duration))
        begin += datetime.timedelta(minutes=60)
        end += datetime.timedelta(minutes=60)
        event_list.append(event)
        duration = f"{end.date()}T{end.time()}+02:00"
        start = f"{begin.date()}T{begin.time()}+02:00"
        print(start)
    return event_list

def open_slot():
    print("Open Slot")
    event_list = open_slots()
    return event_list