import random
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')  # Download the Wordnet dataset

def get_random_word():
    all_words = list(wordnet.all_lemma_names())
    single_words = [word for word in all_words if "_" not in word and "-" not in word and len(word) == 5]
    random_word = random.choice(single_words)
    return random_word
    print(random_word)

def get_user_guess():
    while True:
        guess = input("Please enter your 5-letter English word guess: ")
        if guess.isalpha() and len(guess) == 5:
            return guess.lower()
        else:
            print("Invalid input.")

def compare_words(secret_word, guess):
    used_letters = []
    correct_count = 0
    feedback = ''

    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback += '+'
            used_letters.append(i)
            correct_count += 1
        elif guess[i] in secret_word:
            feedback += '?'
            used_letters.append(i)
        else:
            feedback += '-'

        if correct_count == 4:
            feedback = feedback.replace('?', '-')

    return feedback

def play_game():
    while True:
        # Display the game menu
        print("""****************************************
  /-/- Welcome to the Mystery Words! -/-\
  ****************************************
      (1) Play Game
      (2) About
      (3) Quit
    """)

        choice = input("Enter your choice: ")
        if choice == "1":
            secret_word = get_random_word()
            print(secret_word)
            attempts = 0

            while True:
                guess = get_user_guess()
                attempts += 1

                if guess == secret_word:
                    print("Congratulations! You guessed the correct word.")
                    break

                feedback = compare_words(secret_word, guess)
                print(f"Result: {feedback}")

            print(f"Game over. Total number of attempts: {attempts}")

        elif choice == "2":
            print("""About Mystery Words:
            - Mystery Words is a word guessing game where you have to guess a 5-letter English word.
            - For each guess, you will receive feedback in the form of '+' for correct letters in the correct position, '?' for correct letters in the wrong position, and '-' for incorrect letters.
            - Try to guess the secret word in the fewest attempts possible.
            Have fun!""")

        elif choice == "3":
            print("Quitting the game...")
            break

        else:
            print("Invalid choice. Please try again.")

play_game()
