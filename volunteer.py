import pickle, datetime, getpass, json
from googleapiclient.discovery import build

def create_event(summary, start, duration):
    event = {
        'summary':summary,
        'start': {
            'dateTime': start
        },
        'end':{
            'dateTime': duration
        },
        'attendees':[
            {'email': f"{getpass.getuser()}@student.wethinkcode.co.za"}
        ]
    }
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
    event_list = load_data()

    for amm in range(int(slots)):
        event = insert_event(service, create_event(summary, start, duration))
        begin += datetime.timedelta(minutes=60)
        end += datetime.timedelta(minutes=60)
        event_list['events'].append({getpass.getuser()+'-'+summary+'-'+str(begin.date()) +'-'+str(begin.time()):event})
        duration = f"{end.date()}T{end.time()}+02:00"
        start = f"{begin.date()}T{begin.time()}+02:00"
    return event_list


def open_slot():
    print("Open Slot")
    event_list = open_slots()
    save_data(event_list)
    return event_list


def save_data(event_list):
    with open('event_list.json', 'w') as file:
        json.dump(event_list, file, indent=4)


def load_data():
    with open('event_list.json', 'r') as file:
        event_list = json.load(file)
    return event_list


def remove_event(event_id): 
    service = get_service()
    service.events().delete(calendarId='primary', eventId=event_id).execute()


def cancel_slot():
    print("Please select a slot to cancel:\n")
    events = load_data()
    ava_delete = []
    for item in events['events']:
        for key,items in item.items():
            if getpass.getuser() in key:
                if len(items['attendees']) == 1:
                    ava_delete.append(key)
    for item in range(len(ava_delete)):
        print(f"\t{item + 1}:{ava_delete[item]}")
    cancel = int(input('\n > ')) -1
    event_id = events['events'][cancel][ava_delete[cancel]]['id']
    remove_event(event_id)
    events['events'].pop(cancel)
    save_data(events)
    