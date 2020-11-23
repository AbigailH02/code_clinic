import os
import pickle
import getpass
#we'll add deregister to delete the token

creds = None

def token_exists():
    """checks if the token file exists or not"""

    if os.path.exists('token.pickle'):
        # print('token_exists')
        return True
    return False


def get_creds():
    """gets credentials from the token"""
    with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    return creds


def token_valid():
    """Checks if the token is valid(not expired)"""

    if os.path.exists('token.pickle') and creds and creds.valid:
        # print('Token is valid')
        return True
    return False


def register_user():
    """Creates a new user"""
    print("Please enter your username and password to register")
    user = getpass.getuser()
    print(f'Username: {user}')
    pass1 = getpass.getpass(prompt='Password: ')
    pass_comfirm = getpass.getpass(prompt='Confirm password: ')

    if pass1 == pass_comfirm:
        print(f"Welcome to Code Clinic {user}")
    else:
        print("ERROR! Passwords don't match")


def user_login():
    """"logs in an existing user"""
    print("Please enter your username and password to login")
    user = getpass.getuser()
    print(f'Username: {user}')
    password = getpass.getpass(prompt='Password: ')

    if password == '1234':
        print('logged in succesfully')
    else:
        print("wrong password")

