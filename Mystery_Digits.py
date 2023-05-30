import random

def generate_secret_number():
  digits = random.choices(range(10),k=5)
  return ''.join(map(str,digits))


def get_user_guess():
  while True:
    guess = input("5 haneli bir sayı giriniz..")
    if guess.isdigit() and len(guess) == 5:
      return guess
    else:
      print("Geçersiz giriş.")

def compare_numbers(gsn,guess):
  used_indices = []
  correct_count = 0
  feedback = ''
  
  
  for i in range(5):
    if guess[i] == gsn[i]:
      feedback += '+'
      used_indices.append(i)
      correct_count += 1
    elif guess[i] in gsn and guess[i] != gsn[i]:
      feedback += '?'
      used_indices.append(i)
    else:
      feedback += '-'
    
    if correct_count ==4:
      feedback = feedback.replace("?","-")
  return feedback


def play_game():
  while True:

    print("""**************************************** 
  /-/- Welcome to the Mystery Digits! -\-\ 
  **************************************** 
      (1) Play Game
      (2) About
      (3) Quit
    
    """ )

    choice = input("Enter your choice..")
    if choice == "1":
      
        secret_number = generate_secret_number()
        attempts = 0

        while True:
          guess = get_user_guess()
          attempts += 1

          if guess == secret_number:
            print("Tebrikler...")
            break
          feedback = compare_numbers(secret_number,guess)
          print(f"Sonuç: {feedback}")
    
        print(f"Oyun bitti. Toplam deneme sayısı : {attempts}")
    
    elif choice == "2":
      print(""" About Mystery Digits:        
      - Mystery Digits is a number guessing game where you have to guess a 5-digit number.        
      - For each guess, you will receive feedback in the form of '+' for correct digits in the correct position, '?' for correct digits in the wrong position, and '-' for incorrect digits.        
      - Try to guess the secret number in the fewest attempts possible.        
      Have fun! """)
    elif choice == "3":
      print("Quitting the game...")
      break
    else:
      print("Invalid choice. Please try again...")  

play_game()
