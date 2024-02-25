import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0

    print(f"Guess a number between 1 and {x}.")

    while guess != random_number:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Congratulations! You've guessed the number {random_number} correctly in {attempts} attempts.")

guess(10)
