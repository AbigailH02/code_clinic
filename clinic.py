import login as log
import args as a
import token

def show_commands():
    print("""
    \tWelcome to Wethinkcode's code clinic\n\n
    \tCode Clinic Navigation Tool:\n
    -h, --help          Show this help message
    -register           Used to register a new user.
    -login              Used to login.
    -create_event       Used to create an event.
    -view_events        Used to view all available events.
    -book_event         Used to book an events.
    -delete_event       Used to delete an event.
    """)

def run():
    show_commands()
    user_input = input(">> ")
    while(1):

        if user_input == 'clinic -register' or user_input == 'clinic -r':
            log.registration()
            token.get_token()
        elif user_input == 'clinic -login' or user_input == 'clinic -l':
            log.login()
        
        


if __name__ == "__main__":
    run()