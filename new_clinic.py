import argparse
import authorisation as auth
import textwrap
import os

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
parser.add_argument("-register", help="register new user", action='store_true')
parser.add_argument("-deregister", help="delete user login details", action="store_true")
parser.add_argument("-login", help="Login if already registered in", action="store_true")
args = parser.parse_args()


#checking and executing the commandline arguments
if args.register:
    if not auth.token_exists():
        auth.register_user()
    elif auth.token_exists() and auth.creds_expired():
        user = auth.get_user()
        print(f"You are registered as {user}")
        print("Use this command to login:    clinic -login")
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
        
elif args.deregister:
    if auth.token_exists():
        os.remove("token.pickle")
        print("Deregistration successful.")
    else:
        print(f"\n\t\tUser is not registered\
        \n\n\tcommand to register:   clinic -register\n")


#code below will work if no argument is given
else:#checking if token exists and it's still valid
    if not auth.token_exists():
        print(f"\n\t\tUser is not registered\
        \n\n\tcommand to register:   clinic -register\n")
    elif auth.token_exists() and not auth.token_valid():
        print('\n\t\tUser not logged in')
        print('\t\tcommand to login:     clinic -login\n')
    else:
        print('Welcome to WeThinkCode Code Clinic!')
        auth.get_event()