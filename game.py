import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
print("Welcome to Rock-Paper-Scissors! Best of 3 rounds.\n")
for round_num in range(1, 4):
    print(f"\nRound {round_num}:")
    attempts = 3
    user_choice = None  

    while attempts > 0:
        user_input = input(f"Enter rock, paper, or scissors (You have {attempts} attempts left): ").lower()
        attempts -= 1 
        if user_input in choices:
            user_choice = user_input 
            break
        else:
            print("Invalid choice! Try again.")
    if user_choice is None:
        print("No valid choice made. You lose this round!")
        computer_score += 1
        continue
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("You lose this round!")
        computer_score += 1
    if user_score == 2 or computer_score == 2:
        break
print("\nFinal Score:")
print(f"You: {user_score} | Computer: {computer_score}")
if user_score == computer_score:
    print("The game ends in a tie!")
elif user_score > computer_score:
    print("Congratulations! You won the game!")
else:
    print(" You lost the game! Better luck next time!")
