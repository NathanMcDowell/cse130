# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This project is meant to check if the user-entered username and password are in the system and correct.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was figuring out how to confirm that the password was the correct one for the given 
#       username.Another hard part was a bug that kept returning "unauthorized" even if everything was correct. I figured out that 
#       the problem was that while moving a line of code I had unindented the break keyword. This meant the loop only ran once and
#       and would only work if the user-entered username was the first item on the list. I solved it by going into debug mode and 
#       seeing that the loop was only ever running once.
# 5. How long did it take for you to complete the assignment?
#      It took me 1 hour and 45 minutes to complete this assignment.

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