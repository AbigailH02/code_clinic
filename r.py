import cal
import argparse
import textwrap


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

if args.view_events:
    print("The next ten events from your calendar:\n")
    cal.get_event(service,now)

if args.book_event: 
    print(textwrap.dedent('''
        Here are your slots:

    +----+-------------+-------------+
    | no | available   | Booked      |
    +----+-------------+-------------+
    | 1. | row1column1 | row1column2 |
    | 2. | row2column1 | row2column2 |
    | 3. | row3column1 | row3column2 |
    +----+-------------+-------------+

    book avilable slots by no.(x):

        clinic -book_event x

    (Replace x with a number from the table.)
    '''))

elif args.create_event:
    title = input('Please enter the topic\n > ').strip()
    date = input('Please enter a date [yyyy-mm-dd]\n > ')
    time = input('Please enter a time [hh:mm]\n > ')
    event = cal.create_event(title,date,time)
    print('Event has been created')
    cal.insert_event(service, event)

elif args.delete_event:
    event = cal.get_event(service, now)
    cal.delete_event(service,event)


if __name__ == '__main__':
    pass
