import colorama
import random

CHEATING_MODE = False


def initialise_game():
    try:
        with open("5letters.txt", "r") as file:
            list_of_words = [word.strip() for word in file]
    except FileNotFoundError:
        print("File not found.")
        exit()

    chosen_word = random.choice(list_of_words)
    print(chosen_word) if CHEATING_MODE else None

    displayed_word = [""] * 5  # Format each character of input later on

    word_history = []
    return list_of_words, chosen_word, displayed_word, word_history


# Define colours
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.MAGENTA
GREY = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW


def check_letters(correct_word, guess_word, displayed_word, tried_words, number_of_guesses):
    if guess_word in tried_words:  # Repeated outputs do not add to number of guesses
        return False, number_of_guesses

    tried_words.append(guess_word)  # Stores a list of all entered words for session

    for j in range(0, len(guess_word)):

        if guess_word[j] == correct_word[j]:
            displayed_word[j] = GREEN + guess_word[j]

        elif guess_word[j] in correct_word:
            displayed_word[j] = YELLOW + guess_word[j]

        else:
            displayed_word[j] = GREY + guess_word[j]

    print(*displayed_word)
    # "*" is an unpacking operator; ensures each value from the list is printed on one line

    number_of_guesses += 1

    if guess_word == correct_word:
        return True, number_of_guesses

    return False, number_of_guesses


def get_user_input():
    while True:
        guess = input(GREY + "Enter a five letter word: ")
        if len(guess) != 5:
            continue
        else:
            break
    return guess


if __name__ == "__main__":
    print(("*" * 16) + "\nUNLIMITED WORDLE\n" + ("*" * 16) + "\n")

    wordList, answer, formatted_word, history = initialise_game()

    gameEnd = False
    numGuesses = 0

    while not gameEnd:
        wordInput = get_user_input().lower()

        if wordInput not in wordList:  # Checks to see if word is in dictionary
            print("Invalid word, try again :/")
        else:
            gameEnd, numGuesses = check_letters(answer, wordInput, formatted_word, history, numGuesses)

    print(f"{GREY}Guessed in {numGuesses} goes!") if numGuesses > 1 else print(f"{GREY}Guessed in 1 go!")
