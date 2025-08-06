from random import randint

def play_game():
    # Welcome message
    print("______Welcome to The Game______")
    print("Guess The Number Game")
    bot = randint(1, 100)  # Random number between 1 and 100

    attempts = 1  # Counter for the number of attempts

    # Loop until the user guesses correctly or reaches 10 attempts
    while True:
        try:
            user = int(input("Enter your choice: between 1 to 100: "))

            # Check for invalid input
            if user < 1 or user > 100:
                print(f"Invalid input, please enter a number between 1 and 100.\nYour choice: {user}")
                continue

            # Check if the guess is correct
            if user == bot:
                print(f"You guessed the number {bot} in {attempts} attempts")
                break

            # Check if maximum attempts reached
            elif attempts == 10:
                print(f"You lose, the number was {bot}")
                break

            # Give hints to the user
            elif user > bot:
                print("Lower number please")
                attempts += 1

            elif user < bot:
                print("Higher number please")
                attempts += 1

            # Check for invalid input
            elif user < 1 or user > 100:
                print(f"Invalid input, please enter a number between 1 and 100.\nYour choice: {user}")
        except Exception as error:
            print(f"Something went wrong: {error}")

play_game()