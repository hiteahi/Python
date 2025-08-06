import random

# wlecome
print("______Welcome to The Game______")

# 1 for rock, 0 for paper, -1 for scorreir
print("use 1 for Rock, 0 for Paper, -1 for Scorrier")

    # choise
user = int(input("enter your choose: "))
bot = random.randint(-1, 1)

print(f"")

try:
        # draw
    if user == bot:
        print(f"It's Draw\nyour choose: {user}, bot choose: {bot}")

        #win
    elif user == 1 and bot == -1 or user == 0 and bot == 1 or user == -1 and bot == 0:
        print(f"You Win\nyour choose: {user}, bot choose: {bot}")

        #lose
    elif user == 1 and bot == 0 or user == 0 and bot == -1 or user == -1 and bot == 1:
        print(f"You Lose\nyour choose: {user}, bot choose: {bot}")

        # invalid input
    else:
        print(f"Invalid input, please enter 1, 0, or -1.\nyour choose: {user}")


except Exception as error:
    print("samething went wrong, please try again")

        
