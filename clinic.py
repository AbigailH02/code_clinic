import cal
import argparse
import textwrap

# from cal import service
# from requests import Request

parser = argparse.ArgumentParser(prog='clinic',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Welcome to WeThinkCode Code Clinic!

        A booking tool for Coding Clinic sessions
        --------------------------------------------
            view and edit your coding clinic slots
            book slots created by other members
            cancel or delete slots
        ____________________________________________
        '''))
parser.add_argument("-register", help="Authorise this app to give it permission to access your calendar", action="store_true")
parser.add_argument("-login", help="Login if already registered in", action="store_true")
parser.add_argument("-view_events", help="View all available events", action="store_true")
parser.add_argument("-book_event", help="Book an events for your code clinic", action="store_true")
parser.add_argument("-delete_event", help="Delete an event ", action="store_true")
parser.add_argument("-create_event", help="create an event ", action="store_true")
args = parser.parse_args()

service,now = cal.main()
# print(args)
if args.view_events:
    cal.get_event(service,now)
    print(textwrap.dedent('''
    These are your events:

    +-------------+-------------+
    | Booked      | Volunteered |
    +-------------+-------------+
    | row1column1 | row1column2 |
    | row2column1 | row2column2 |
    | row3column1 | row3column2 |
    +-------------+-------------+
    '''))

if args.book_event:
    print("hello") 

elif args.create_event:
    # service,now = cal.main()
    title = input('Please enter the topic\n > ').strip()
    date = input('Please enter a date [yyyy-mm-dd]\n > ')
    time = input('Please enter a time [hh:mm]\n > ')
    event = cal.create_event(title,date,time)
    print('Event has been created')
    cal.insert_event(service, event)
    print(event)

elif args.delete_event:
    # service,now = cal.main()
    event = cal.get_event(service, now)
    cal.delete_event(service,event)


# elif args.delete_event:
    # print("hello")

if __name__ == '__main__':
    pass