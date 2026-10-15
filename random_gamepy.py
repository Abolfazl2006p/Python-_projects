import random
secret = random.randint(1, 10)
guess = int(input("guess a number (1-10): "))
if guess == secret:
    print("you win")
else:
    print("you lose! the number was", secret)
        