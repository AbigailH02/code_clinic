import argparse
import json
import stdiomask


parser = argparse.ArgumentParser(prog="clinic",description="A booking tool for Wethinkcode's code clinic")
parser.add_argument("-register", help="Used to register a new user.", action='store_true')
parser.add_argument("-login", help="Used to login.", action="store_true")
parser.add_argument("-view_events", help="Used to view all available events.", action="store_true")
parser.add_argument("-book_event", help="Used to book an events.", action="store_true")
parser.add_argument("-delete_event", help="Used to delete an event.", action="store_true")
parser.add_argument("-create_event", help="Used to create an event.", action="store_true")
args = parser.parse_args()


def confirm_password(password):
    while (len(password) < 6):
        print("Password must be a minumum of 6 characters.")
        password = stdiomask.getpass(prompt = "Enter your password: ").strip()

    while(True):
        confirm_password = stdiomask.getpass(prompt = "Confirm your password: ").strip()
        if confirm_password == password:
            break
        else:
            print("ERROR: Password don't match")
            continue
    return password


def new_username(name, filename="secret.json"):
    with open(filename) as json_file:
        user_info = json.load(json_file)

    new_list = user_info["user_information"]
    
    while (True):
        if any(dictionary["name"] == name for dictionary in new_list):
            print("Username already exist")
            name = input("Enter new username: ").strip().lower()
            continue
        break  
    return name


def get_user(register): 

    name = input("Enter your username: ").strip().lower()
    if register == True:
        name = new_username(name)

    password = stdiomask.getpass(prompt = "Enter your password: ").strip()
    if register == True:
        password = confirm_password(password)
    user_details = {
        "name" : name,
        "password" : password,
        "email" : name + "@student.wethinkcode.co.za"
    }

    return user_details


def registration(filename='secret.json'):
    with open(filename) as json_file: 
        data = json.load(json_file)

    temp = data['user_information']
    temp.append(get_user(True))

    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


def login(filename='secret.json'):
    login_info = get_user(False)

    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
    
    if login_info in json_object["user_information"]:
        print("Login sucessful")
    else:
        print("Incorrect username or password")