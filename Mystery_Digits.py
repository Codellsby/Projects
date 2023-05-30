import random

def generate_secret_number():
    # Generate a random 5-digit secret number
    digits = random.choices(range(10), k=5)
    return ''.join(map(str, digits))


def get_user_guess():
    while True:
        # Prompt the user to enter a 5-digit guess
        guess = input("Enter a 5-digit number: ")
        if guess.isdigit() and len(guess) == 5:
            return guess
        else:
            print("Invalid input. Please enter a valid 5-digit number.")


def compare_numbers(secret_number, guess):
    used_indices = []
    correct_count = 0
    feedback = ''

    # Compare each digit of the guess with the secret number
    for i in range(5):
        if guess[i] == secret_number[i]:
            feedback += '+'
            used_indices.append(i)
            correct_count += 1
        elif guess[i] in secret_number and guess[i] != secret_number[i]:
            feedback += '?'
            used_indices.append(i)
        else:
            feedback += '-'

        # If four digits are correct, replace '?' with '-' to avoid confusion
        if correct_count == 4:
            feedback = feedback.replace("?", "-")

    return feedback


def play_game():
    while True:
        # Display the game menu
        print("""****************************************
  /-/- Welcome to the Mystery Digits! -\-\ 
  ****************************************
      (1) Play Game
      (2) About
      (3) Quit
    """)

        choice = input("Enter your choice: ")
        if choice == "1":
            # Start a new game
            secret_number = generate_secret_number()
            attempts = 0

            while True:
                # Get user's guess and provide feedback
                guess = get_user_guess()
                attempts += 1

                if guess == secret_number:
                    print("Congratulations! You guessed the correct number.")
                    break
                feedback = compare_numbers(secret_number, guess)
                print(f"Result: {feedback}")

            print(f"Game over. Total attempts: {attempts}")

        elif choice == "2":
            # Provide information about the game
            print("""About Mystery Digits:
      - Mystery Digits is a number guessing game where you have to guess a 5-digit number.
      - For each guess, you will receive feedback in the form of '+' for correct digits in the correct position,
        '?' for correct digits in the wrong position, and '-' for incorrect digits.
      - Try to guess the secret number in the fewest attempts possible.
      Have fun!""")

        elif choice == "3":
            # Quit the game
            print("Quitting the game...")
            break

        else:
            print("Invalid choice. Please try again...")


# Start the game
play_game()
