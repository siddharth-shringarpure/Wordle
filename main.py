import colorama
import random


def initialise_game():
    try:
        with open("5letters.txt", "r") as file:
            wordList = [word.strip() for word in file]
    except FileNotFoundError:
        print("File not found.")
        exit()

    answer = random.choice(wordList)
    # print(answer)
    displayed_word = [""] * 5  # Format each character of input later on

    history = []
    return wordList, answer, displayed_word, history


# Define colours
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.MAGENTA
GREY = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW


def check_letters(answer, guess_word, displayed_word, history, guesses):
    if guess_word in history:  # Repeated outputs do not add to number of guesses
        return False, guesses

    history.append(guess_word)  # Stores a list of all entered words for session

    for j in range(0, len(guess_word)):

        if guess_word[j] == answer[j]:
            displayed_word[j] = GREEN + guess_word[j]

        elif guess_word[j] in answer:
            displayed_word[j] = YELLOW + guess_word[j]

        else:
            displayed_word[j] = GREY + guess_word[j]

    print(*displayed_word)
    # "*" is an unpacking operator; ensures each value from the list is printed on one line

    guesses += 1

    if guess_word == answer:
        return True, guesses

    return False, guesses


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

    wordList, answer, displayed_word, history = initialise_game()

    gameEnd = False
    guesses = 0

    while not gameEnd:
        wordInput = get_user_input().lower()

        if wordInput not in wordList:  # Checks to see if word is in dictionary
            print("Invalid word, try again :/")
        else:
            gameEnd, guesses = check_letters(answer, wordInput, displayed_word, history, guesses)

    print(f"{GREY}Correctly guessed in {guesses} goes!") if guesses > 1 else print(f"{GREY}Correctly guessed in 1 go!")
