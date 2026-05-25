
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Python Hangman game that uses loops, conditionals, strings, and user input to let players guess a hidden word one letter at a time.

## 📝 Tasks

### 🛠️ Build the Game Engine

#### Description

Create the core Hangman logic to select a word, track guesses, and display progress as the player attempts to guess letters.

#### Requirements
Completed program should:

- Choose a random word from a predefined list
- Display the current word progress using underscores for unknown letters (e.g., `_ a _ _ m a n`)
- Track correct and incorrect guesses separately
- Limit the number of incorrect guesses allowed

### 🛠️ Add Player Interaction and End Conditions

#### Description

Implement the user input loop and game ending logic so the player can guess letters until they win or lose.

#### Requirements
Completed program should:

- Prompt the player to guess a letter each turn
- Update the displayed progress after each valid guess
- Detect when the player has guessed the full word
- Show a win message if the player succeeds and a lose message if attempts run out
- Prevent repeated letter guesses from affecting the remaining attempts
