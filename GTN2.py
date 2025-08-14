from random import randint

def play_game():
    print("=" * 40)
    print(" " * 7 + "Welcome to The Game")
    print(" " * 5 + "Guess The Number Game")
    print("=" * 40)

    user_score = 0 

    while True:
        try:
            rounds = int(input("\nHow many rounds would you like to play? "))
            if rounds < 1:
                print("⚠️  Please enter a positive integer for rounds.")
                continue
            break
        except ValueError:
            print("⚠️  Invalid input, please enter a valid integer.")

    for round_num in range(1, rounds + 1):
        bot = randint(1, 100)
        attempts = 1
        print("\n" + "-" * 40)
        print(f"🔵 Round {round_num} of {rounds}".center(35))
        print("-" * 40)

        while True:
            try:
                user = input(f"Attempt {attempts}/10 - Enter your guess (1-100): ")
                user = int(user)

                if user < 1 or user > 100:
                    print(f"⚠️  Please enter a number between 1 and 100. You entered: {user}")
                    continue

                if user == bot:
                    print(f"🎉 Correct! You guessed the number {bot} in {attempts} attempts.")
                    user_score += 1
                    break
                elif attempts == 10:
                    print(f"❌ Out of attempts! The number was {bot}.")
                    break
                elif user > bot:
                    print("🔻 Too high! Try a lower number.")
                    attempts += 1
                elif user < bot:
                    print("🔺 Too low! Try a higher number.")
                    attempts += 1
            except ValueError:
                print("⚠️  Invalid input, please enter a number.")
            except Exception as error:
                print(f"⚠️  Something went wrong: {error}")

    print("\n" + "=" * 40)
    print(f"🏆 Game Over! Your final score: {user_score} out of {rounds}")
    print("=" * 40)

play_game()
