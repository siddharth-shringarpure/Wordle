import colorama
import random

CHEATING_MODE = False
GAME_NAME = "WORDLE"


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


def check_letters(correct_word, user_guess, displayed_word, tried_words, number_of_guesses):
    if user_guess in tried_words:  # Repeated outputs do not add to number of guesses
        return False, number_of_guesses

    tried_words.append(user_guess)  # Stores a list of all entered words for session

    for j in range(0, len(user_guess)):

        if user_guess[j] == correct_word[j]:
            displayed_word[j] = GREEN + user_guess[j]

        elif user_guess[j] in correct_word:
            displayed_word[j] = YELLOW + user_guess[j]

        else:
            displayed_word[j] = GREY + user_guess[j]

    print(*displayed_word)
    # "*" is an unpacking operator; ensures each value from the list is printed on one line

    number_of_guesses += 1

    if user_guess == correct_word:
        return True, number_of_guesses

    return False, number_of_guesses


def get_user_input():
    while True:
        user_input = input(GREY + f"Enter a five letter word ({numGuesses+1} / {maxGuesses}): ")
        if len(user_input) != 5:
            continue
        else:
            break
    return user_input


def get_number_of_guesses():
    while True:
        try:
            input_guesses = input(GREY + "How many guesses? (press Enter for default: 5, 'inf' for unlimited): ")
            if not input_guesses:
                return 5
            elif input_guesses.lower() == "inf":
                return float("inf")  # Infinite guesses
            else:
                guesses = int(input_guesses)
                if guesses > 0:
                    return guesses
                else:
                    print("Number of guesses must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    divider_length = len(GAME_NAME) * 3
    print(f"{'*' * divider_length}\n"
          f"{' ' * int(0.5 * (divider_length - len(GAME_NAME)))}"
          f"{GAME_NAME}\n{'*' * divider_length}")

    wordList, answer, formatted_word, history = initialise_game()

    gameEnd = False
    numGuesses = 0
    maxGuesses = get_number_of_guesses()

    while (not gameEnd) and (numGuesses < maxGuesses):
        wordInput = get_user_input().lower()

        if wordInput not in wordList:  # Checks to see if word is in dictionary
            print("Invalid word, try again :/")
        else:
            gameEnd, numGuesses = check_letters(answer, wordInput, formatted_word, history, numGuesses)

    if numGuesses >= maxGuesses:
        print(f"Out of guesses! The correct word was {GREEN}{answer}.")
    else:
        print(f"{GREY}Guessed in {numGuesses} goes!") if numGuesses > 1 else print(f"{GREY}Guessed in 1 go!")
