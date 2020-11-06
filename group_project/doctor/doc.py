import mutual_assist.mutual_assist

def help():
    # user = input("You are aware that you volunteering to be a doctor\nYes\nNo\n")
    # user = user.lower()
    # if user == "yes":
    print("That is great. Time to pick a topic.")
    mutual_assist.mutual_assist.topics()
    # elif user == "no":
    #     print("Oh.That is okay!")