import random

print("Welcome to the Number Guessing Game!")
print("I picked a number between 1 and 10.")

secret_number = random.randint(1, 10)

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Correct! You guessed it.")
elif guess < secret_number:
    print("Too low. Try again.")
else:
    print("Too high. Try again.")

print("The secret number was", secret_number)
