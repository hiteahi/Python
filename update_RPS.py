import random
def game():
    print("=" * 40)
    print(" Welcome to The Game ".center(40, "-"))
    print(" Rock Paper Srissors ".center(40, "-"))
    print("=" * 40)

    # Mapping choices
    youdict = {"s": 1, "w": -1, "g": 0}
    # reverse_dict = {1: "snake", -1: "water", 0: "gun"}

    # Initialize scores
    user_score = 0
    computer_score = 0

    # Number of rounds
    rounds = int(input("\nHow many rounds would you like to play? "))

    for round_num in range(1, rounds + 1):
        
        print()
        print(f"Round {round_num}".center(40, "-"))

        computer = random.choice([1, -1, 0])

        print(" s for Snake, w for Water, g for Gun".center(40, "-"))
        youstr = input("Enter your choice: ").lower()
        print()
    
        if youstr not in youdict:
            print("Invalid input! You lose this round.")
            computer_score += 1
            continue

        you = youdict[youstr]

        # print(f"You chose: {reverse_dict[you]}".center(40, " "))
        # print(f"Computer chose: {reverse_dict[computer]}".center(40, " "))

        if computer == you:
            print("It's a draw!".center(40, " "))
        elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You win this round!".center(40, " "))
            user_score += 1
        else:
            print("Computer wins this round!".center(40, " "))
            computer_score += 1
    
        

    # Final result
    print("=" * 40)
    print("Game Over".center(40, " "))
    print(f"Your Score: {user_score}".center(40, " "))
    print(f"Computer Score: {computer_score}".center(40, " "))
    print()

    if user_score > computer_score:
        print("You won the game!🎉".center(40, "-"))
    elif user_score < computer_score:
        print("Computer won the game!😢".center(40, "-"))
    else:
        print("It's a tie!🤝".center(40, "-"))

    print("=" * 40)
    
game()
