import doctor.doc
import patient.patient
print("Welcome to Code Clinic!")

user = input("Are you in need of assistance?\nYes\nNo\n")
user = user.lower()
if user == "yes":
    patient.patient.help_needed()
elif user == "no":
    user2 = input("Would you like to volunteer to assist?\nYes\nNo\n")
    user2 = user2.lower()
    if user2 == "yes":
        doctor.doc.help()
    
