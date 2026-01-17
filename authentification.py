# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

def main():
    with open("Lab02.json", "rt") as filehandle: # Pulls the data from a json file to make a list
        data = json.load(filehandle)
    username_attempt = "0"
    password_attempt = "0"

    while username_attempt != "q" and password_attempt != "q":
        authenticated = False
        username_attempt = input("Username: ")
        password_attempt = input("Password: ")
        print()
        for username in data["username"]: # Runs through every item in the username list to see if it is there.
            if username_attempt == username: # If it is:
                for password in data["password"]: # Check the password list to see if the password is there.
                    if password_attempt == password: # If it is:
                        if data["username"].index(username_attempt) == data["password"].index(password_attempt): # Check if the username and password share the same index.
                            print("You are authenticated!")
                            authenticated = True
                break # Break out of the loop so that you don't run the program more than needed.
        if authenticated == False:
            print("You are not authorized to use the system.")


main()