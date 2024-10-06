import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attemps = 0
    while True:
        user_guess = int(input("Guess the number (between 1 and 100):"))
        attemps += 1
        if user_guess < number_to_guess:
            print ("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Cong9ratz! You guessed the number in {attemps} attempts.")
            break
guess_the_number()