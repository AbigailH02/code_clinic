import argparse
import authorisation as auth
import volunteer

parser = argparse.ArgumentParser(prog="clinic",description="a booking tool for Wethinkcode's code clinic")

parser.add_argument("-register", help="register new user", action='store_true')
parser.add_argument("-login", help="Login if already registered in", action="store_true")
parser.add_argument("-open", help="Opens a slot from a volunteer", action="store_true")
parser.add_argument("-cancel", help="Cancels a volunteers slot", action="store_true")

args = parser.parse_args()


#checking and executing the commandline arguments
if args.register:
    if not auth.token_exists():
        auth.register_user()
    else:
        print(f"You are registered as {auth.get_user()}")

elif args.login:
    if auth.token_exists() and not auth.token_valid():
        auth.user_login()
    elif not auth.token_exists():
        print(f"\n\t\tUser is not registered\
        \n\n\tcommand to register:   clinic -register\n")
    else:
        print(f"You are logged in as {auth.get_user()}")

elif args.open:
    events = volunteer.open_slot()

elif args.cancel:
    volunteer.cancel_slot()

#code below will work if no argument is given
#checking if token exists and it's still valid
else:
    if not auth.token_exists():
        print(f"\n\t\tWelcome to Code Clinic!\n\t\tUser is not registered\
        \n\n\tcommand to register: clinic -register\n\n\
        command to login: clinic -login\n\
        \n\tFor all navigation commands: clinic -help\n")
    elif auth.token_exists() and not auth.token_valid():
        print('\n\t\tUser not logged in')
        print('\t\tcommand to login:     clinic -login\n')
    else:
        print('Welcome to Code Clinic')
        auth.get_event()

