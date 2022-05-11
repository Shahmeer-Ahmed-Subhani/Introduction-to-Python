try:
    user_input = str(input(("Is your internet working? ")))
except ValueError:
    (print("Invalid Input"))


if user_input == "yes":
    print("I bet you don't lag on call")
elif user_input == "no": 
    print("Get a better internet you idiot")
else:
    print("Please input in yes or no and restart this program")