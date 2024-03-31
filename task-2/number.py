
def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize variables
    guessed = False
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("Try to guess the number between 1 and 100.")

    while not guessed:
        try:
            # Get user input for the guess
            user_guess = int(input("Enter your guess: "))

            # Increment the attempts counter
            attempts += 1

            # Check if the guess is correct
            if user_guess == secret_number:
                guessed = True
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            else:
                # Provide hints
                if user_guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
