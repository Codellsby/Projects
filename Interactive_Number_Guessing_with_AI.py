import random

ai_number = random.randint(0, 100)

while True:
    # Prompt the user for a guess
    human_guess = int(input("Enter your guess: "))

    if human_guess > ai_number:
        # If the guess is higher than the AI's number, provide a hint to try a smaller number
        print("Try a smaller number.")
    elif human_guess < ai_number:
        # If the guess is lower than the AI's number, provide a hint to try a larger number
        print("Try a larger number.")
    else:
        # If the guess is equal to the AI's number, congratulate the user and end the loop
        print("Congratulations, you guessed it!")
        break
