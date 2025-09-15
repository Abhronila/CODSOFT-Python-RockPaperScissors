import random
choices = ["rock", "paper", "scissors"]

def play_round():
    while  True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in choices:
            break
        else:
            print("❌Invalid choice! Please enter rock, paper, or scissors.")
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif(user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        return "player"
    else:
        print("You lose!")
        return "computer"

play_again = "yes"
first_match = True
while play_again == "yes":
    if first_match:
        print("\nStarting a 5 round match!")
        first_match = False
    else:
        print("\nStarting another 5 round match!")

    player_score = 0
    computer_score = 0
    ties = 0

    for i in range(5):
        print(f"\nRound {i+1}:")
        result = play_round()

        if result == "player":
            player_score +=1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1

    print("\n📊Match Results:")
    print(f"PLayer Scored: {player_score}")
    print(f"Computer Scored: {computer_score}")
    print(f"Ties: {ties}")

    if player_score > computer_score:
        print("🏆 You won this match!")
    elif computer_score > player_score:
        print("💻 Computer won this match!")
    else:
        print("🤝 The match is a tie!")
              
    play_again = input("Do you want to play again?(yes/no): ").lower()
    