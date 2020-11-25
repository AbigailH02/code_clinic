import argparse
import authorisation as auth

parser = argparse.ArgumentParser(prog="clinic",description="a booking tool for Wethinkcode's code clinic")

parser.add_argument("-register", help="register new user", action='store_true')
parser.add_argument("-login", help="Login if already registered in", action="store_true")

args = parser.parse_args()



if args.register:
    auth.register_user()
elif args.login:
    auth.user_login()
else:
    if not auth.token_exists():
        print(f"\n\t\tUser is not registered\
        \n\n\tcommand to register:   clinic -register\n")
    elif auth.token_exists() and not auth.token_valid():
        print('\n\t\tUser not logged in')
        print('\t\tcommand to login:     clinic -login\n')
    else:
        print('Welcome to code')
