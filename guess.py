import random
secret = random.randint(1, 100)
guess = 0
attempts = 0
while guess != secret:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
                