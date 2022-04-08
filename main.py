import random, colorama
# Colorama: use "+" when printing a colour before a string/other data type to ensure a blank space is not created

file = open("5letters.txt","r"); wordList = file.readlines()

# Add each item from file to a list of words and remove new line character from each word
for i in range(0,len(wordList)):
    wordList[i] = str(wordList[i]).strip("\n")

green = colorama.Fore.GREEN
red = colorama.Fore.MAGENTA
grey = colorama.Fore.RESET
yellow = colorama.Fore.YELLOW


answer = random.choice(wordList)
#print(answer)
displayList = [""] * 5


def letterFinder(wordInput):
    global guesses
    global gameEnd

    for i in range(0, len(wordInput)):

        if wordInput[i] == answer[i]:
            #print("yes", str(i), "position")
            displayList[i] = green + wordInput[i]

        elif wordInput[i] in answer:
            #print("letter: ", input[i], "in answer")
            displayList[i] = yellow + wordInput[i]

        else:
            displayList[i] = grey + wordInput[i]

    print(*displayList)
    # "*" is an unpacking operator; ensures each value from the list is printed on one line

    guesses+=1

    if wordInput == answer:
        gameEnd = True


def guessFunct():
    while 0 != 2:
        guess = input(grey + "Enter a five letter word: ")
        if len(guess) != 5:
            None
        else:
            break
    return guess

gameEnd = False
guesses = 0

while gameEnd == False:
    wordInput = guessFunct()
    #gameEnd = letterFinder(wordInput)
    letterFinder(wordInput.lower())

#print(grey + "Correctly guessed in:", guesses, "goes!")
print(grey + f"Correctly guessed in {guesses} goes!") if guesses > 1 else print(grey + f"Correctly guessed in {guesses} go!")

file.close()