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
    with open("Lab02.json", "rt") as filehandle:
        data = json.load(filehandle)

    user_input = ""
    while user_input != "q":
        username_attempt = input("Username: ")
        # password_attempt = input("Password: ")
        for i in data["password"]:
            print(i)


main()