import json
import stdiomask


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


def main():
    
    
    status = input("Are you a registered user?\ny/n : ").strip().lower()
    if status == 'n':
        registration()
    elif status == 'y':
        login()

if __name__ == "__main__":
    main()
