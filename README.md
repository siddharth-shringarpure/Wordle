# 👉 Wordle (clone)


![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg "Made with Python")


My attempt at remaking the [original](https://www.nytimes.com/games/wordle/index.html).

## ℹ️ Requirements
- colorama (for colour-coding letters)

## 💡 Features
- CLI based and supports colour-coded output
- Re-guessing a previously guessed word doesn't increase total number of guesses
- Supports an unlimited number of guesses

## 🤔 How to Play

> **Objective**: Guess a hidden five-letter English word in 6 attempts
- The letters can only be used once in a single guess


- After each guess, the game provides feedback on your letters by colouring them
  - Grey: incorrect letter
  - Yellow: letter is in the word, but in the wrong position
  - Green: letter is in the correct position in the word


- If you guess the correct word in 6 attempts, you win!
- If you don't guess the correct word within six attempts, the game ends.