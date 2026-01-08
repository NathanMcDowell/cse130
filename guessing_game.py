import random
high_number = 10
def main():
    target_number = random.choice(range(1, high_number + 1))
    print(target_number)
    print(f"Try to guess a number between 1 and {high_number}")
    user_number = 0
    guesses_remaining = 3
    while user_number != target_number and guesses_remaining > 1:
        try:
            user_number = int(input("> "))
            if user_number == target_number:
                print("Congratulations! You got the number.")
            elif user_number > target_number:
                print("Too high!")
                
            elif user_number < target_number:
                print("Too low!")
        except ValueError:
            print("Please give an integer.")
        
        
            
    



main()