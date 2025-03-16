import random

def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Step 2: Set the number of attempts
    max_attempts = 10
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"Enter number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
    # Step 3: Start the guessing loop
    while attempts < max_attempts:
        try:
            # Step 4: Get the player's guess
            guess = int(input("Enter your guess: "))
            
            # Step 5: Increment the number of attempts
            attempts += 1
            
            # Step 6: Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                return  # End the game if the guess is correct
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Step 7: If the player runs out of attempts
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

# Step 8: Run the game
if __name__ == "__main__":
    number_guessing_game()