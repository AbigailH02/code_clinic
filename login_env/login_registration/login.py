import getpass
import stdiomask

user = {}
status = ""

def registration():
    status = input("Are you a registered user? y/n? Press e to exit\n")
    if status == 'y':
        oldUser()
    elif status == 'n':
        newUser()
    

def newUser():
    createLogin = input("Create login name:")

    if createLogin in user:
        print("\nLogin name already exists.\n")
    else:
        print(
    '''Password must be a minumum of 6 characters and a maximum of 8 characters.''')

    createPass = stdiomask.getpass(prompt = "Enter password:")
    if len(createPass) < 6:
        print("Your password is too short.")
        newUser()
    elif len(createPass) > 8:
        print("Your password is too long")
        newUser()
    elif 6 < len(createPass) < 8:
        user[createLogin] = createPass
        print("User created.\n")


def oldUser():
    login = input("Enter login name:")
    password = stdiomask.getpass(prompt = "Enter password:")

    if login in user and user[login] == password:
        print("\nLogin successful")
    else:
        print("\nUser does not exist or password is incorrect.")
        oldUser()

while status != 'e':
    registration()

    
