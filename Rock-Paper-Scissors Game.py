import random

def rock_paper_scissors():
    # Step 1: Define the choices
    choices = ["rock", "paper", "scissors"]
    
    # Step 2: Initialize scores
    player_score = 0
    computer_score = 0
    ties = 0
    
    # Step 3: Welcome message
    print("Welcome to Rock-Paper-Scissors!")
    print("You will be playing against the computer.")
    print("Enter your choice: rock, paper, or scissors.")
    
    # Step 4: Ask the player how many rounds they want to play
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? (Best of 3, 5, etc..): "))
            if rounds > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Step 5: Start the game loop
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        
        while True:
            # Step 6: Get the player's choice
            player_choice = input("Your choice: ").lower()
            
            # Step 7: Validate the player's choice
            if player_choice not in choices:
                print("Invalid choice! Please choose rock, paper, or scissors.")
            else:
                break  # Exit the loop if the choice is valid
        
        # Step 8: Get the computer's choice
        computer_choice = random.choice(choices)
        
        # Step 9: Display choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Step 10: Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations! You win this round!")
            player_score += 1
        else:
            print("Sorry, you lose this round!")
            computer_score += 1
        
        # Step 11: Display current scores
        print(f"\nScores after Round {round_num}:")
        print(f"Player: {player_score} | Computer: {computer_score} | Ties: {ties}")
    
    # Step 12: Determine the overall winner
    print("\nGame Over!")
    print(f"Final Scores: Player: {player_score} | Computer: {computer_score} | Ties: {ties}")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Sorry, you lost the game.")
    else:
        print("The game is a tie!")

# Step 13: Run the game
if __name__ == "__main__":
    rock_paper_scissors()