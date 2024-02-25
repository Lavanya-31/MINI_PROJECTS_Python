import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of allowed incorrect guesses

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\n" + display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts -= 1
                print(f"Incorrect! {attempts} attempts remaining.")
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letters) == set(secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", secret_word)

hangman()
