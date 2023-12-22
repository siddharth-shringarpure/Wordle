import colorama
import random

file = open("5letters.txt", "r")
wordList = file.readlines()
numWords = len(wordList)

# Add each item from file to a list of words and remove new line character from each word
for i in range(0, numWords):
    wordList[i] = str(wordList[i]).strip("\n")

GREEN = colorama.Fore.GREEN
RED = colorama.Fore.MAGENTA
GREY = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

answer = random.choice(wordList)
print(answer)
formattedInput = [""] * 5  # Format each character of input later on

history = []

def check_letters(guess_word):
    global guesses, gameEnd, history

    if guess_word in history:  # Checks to see if user has repeated an input
        return
    else:
        history.append(guess_word)  # Stores a list of all entered words for session

    for j in range(0, len(guess_word)):

        if guess_word[j] == answer[j]:
            # print("yes", str(i), "position")
            formattedInput[j] = GREEN + guess_word[j]

        elif guess_word[j] in answer:
            # print("letter: ", input[i], "in answer")
            formattedInput[j] = YELLOW + guess_word[j]

        else:
            formattedInput[j] = GREY + guess_word[j]

    print(*formattedInput)
    # "*" is an unpacking operator; ensures each value from the list is printed on one line

    guesses += 1

    if guess_word == answer:
        gameEnd = True


def get_user_input():
    while True:
        guess = input(GREY + "Enter a five letter word: ")
        if len(guess) != 5:
            None
        else:
            break
    return guess


gameEnd = False
guesses = 0

print(("*" * 16) + "\nUNLIMITED WORDLE\n" + ("*" * 16) + "\n")

while not gameEnd:
    wordInput = get_user_input().lower()
    # gameEnd = letterFinder(wordInput)

    if wordInput not in wordList:  # Checks to see if word is in dictionary
        print("Not in dict :/")
    else:
        check_letters(wordInput)

# print(GREY + "Correctly guessed in:", guesses, "goes!")
print(GREY + f"Correctly guessed in {guesses} goes!") if guesses > 1 else print(
    GREY + f"Correctly guessed in {guesses} go!")

file.close()
