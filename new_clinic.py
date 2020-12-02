import argparse
import authorisation as auth

parser = argparse.ArgumentParser(prog="clinic",description="a booking tool for Wethinkcode's code clinic")

parser.add_argument("-register", help="register new user", action='store_true')
parser.add_argument("-login", help="Login if already registered in", action="store_true")

args = parser.parse_args()


#checking and executing the commandline arguments
if args.register:
    if not auth.token_exists():
        auth.register_user()
    else:
        print(f"You are logged in as {auth.get_user()}")

elif args.login:
    if auth.token_exists() and not auth.token_valid():
        auth.user_login()
    elif not auth.token_exists():
        print(f"\n\t\tUser is not registered\
        \n\n\tcommand to register:   clinic -register\n")
    else:
        print(f"You are logged in as {auth.get_user()}")

#code below will work if no argument is given
else:#checking if token exists and it's still valid
    if not auth.token_exists():
        print(f"\n\t\tUser is not registered\
        \n\n\tcommand to register:   clinic -register\n")
    elif auth.token_exists() and not auth.token_valid():
        print('\n\t\tUser not logged in')
        print('\t\tcommand to login:     clinic -login\n')
    else:
        print('Welcome to Code Clinic')
        auth.get_event()

