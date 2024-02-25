import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    print(f"Think of a number between 1 and {x}.")

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

    print(f"The computer guessed your number, {guess}, correctly!")

computer_guess(10)
