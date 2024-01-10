import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "gaming", "openai", "language"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6

    while True:
        print("\nAttempts left:", attempts_left)
        current_display = display_word(secret_word, guessed_letters)
        print(current_display)

        if current_display == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                attempts_left -= 1
                guessed_letters.append(guess)
                if attempts_left == 0:
                    print("Sorry, you ran out of attempts. The word was:", secret_word)
                    break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
