# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      The program picks a random number and gives hints as the user tries to guess it.
# 4. What was the hardest part? Be as specific as possible.
#      This project wasn't very hard. I would say that that part that was most annoying
#      was trying to get OBS to work so I could make the video. It kept crashing and
#      eventually I settled on a phone recording. In the project, the hardest part was
#      protecting the program from non-integer user entry using a try/except. I also 
#      had a problem with the instructions. They wouldn't load for me, so I had to work
#      without all the requirements. I have that fixed now, and I am adding the parts I
#      didn't before.
# 5. How long did it take for you to complete the assignment?
#      It took me about an hour to make the program.

import random
def main():
    high_number = 0
    while high_number <= 0:
        try:
            print("Input a positive number.")
            high_number = int(input("> "))
        except ValueError:
            print("That is not valid.")
            high_number == 0

    target_number = random.choice(range(1, high_number + 1))
    user_number = 0
    starting_guesses = high_number//2
    guesses_remaining = starting_guesses
    # print(f"Debug - Target Number: {target_number}")
    print(f"Try to guess a number between 1 and {high_number}")
    print(f"You have {starting_guesses} guesses")
    while user_number != target_number and guesses_remaining > 0:
        try:
            user_number = int(input("> "))
            if user_number == target_number:
                print("Congratulations! You got the number.")
                print(f"It took you {starting_guesses-guesses_remaining+1} guesses.")
            elif user_number > target_number:
                guesses_remaining -= 1
                print(f"Too high! You have {guesses_remaining} guesses left.")
            elif user_number < target_number:
                guesses_remaining -= 1
                print(f"Too low! You have {guesses_remaining} guesses left.")
            if guesses_remaining <= 0:
                print("You are out of guesses!")
                print(f"The number was {target_number}")
        except ValueError:
            print("Please give an integer.")
        
        
            
    



main()