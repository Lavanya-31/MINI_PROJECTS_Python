import random

def play():
    choices = ['rock', 'paper', 'scissors']
    
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Congratulations! You won!"
    else:
        return "Sorry, you lost!"

print(play())
