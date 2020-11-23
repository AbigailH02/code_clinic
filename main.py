import json


def get_user(): 

    name = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    user_details = {
        "name" : name,
        "password" : password
    }
    return user_details


def register(filename='secret.json'):
    with open(filename) as json_file: 
        data = json.load(json_file)

    temp = data['user_infomation']
    temp.append(get_user())

    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 


def login(filename='secret.json'):
    login_info = get_user()

    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
    
    if login_info in json_object["user_infomation"]:
        print("Sucessful Login")
    else:
        print("Incorrect username or password")


#register()
login()