import volunteer
import getpass


def create_booking():
    events = volunteer.load_data()
    email = {'email': 'ajenkins' + '@student.wethinkcode.co.za'}

    print("Please select a slot to book:\n")
    available_slots = []
    for item in events['events']:
        for key,items in item.items():
            if len(items['attendees']) == 1:
                available_slots.append(key)

    for item in range(len(available_slots)):
        print(f"\t{item + 1}:{available_slots[item]}")


    book = int(input('\n > ')) -1

    event_id = events['events'][book][available_slots[book]]['id']


    events['events'][book][available_slots[book]]['attendees'].append(email)

    service = volunteer.get_service()
    updated_event = service.events().update(calendarId='primary', eventId=event_id, body=events['events'][book][available_slots[book]]).execute()

    volunteer.save_data(events)


create_booking()