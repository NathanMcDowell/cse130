import random
high_number = 10
def main():
    target_number = random.choice(range(1, high_number + 1))
    user_number = 0
    starting_guesses = high_number//2
    guesses_remaining = starting_guesses
    print(f"Debug Target Number: {target_number}")
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