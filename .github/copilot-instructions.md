# Hangman Game - AI Coding Agent Instructions

## Project Overview
This is a Python implementation of the classic Hangman word-guessing game. The game randomly selects a word, hides it with dashes, and allows users to guess letters with a maximum of 6 failed attempts.

## Core Game Architecture

### Main Game Loop Components
1. **Word Selection**: Use `random.choice()` to select from a predefined word list
2. **Display State**: Maintain two representations - actual word and display (dashes with guessed letters)
3. **Input Validation**: Accept only single, previously-unguessed letters using try-except blocks
4. **Attempt Tracking**: Count failed guesses (letters not in word) up to 6 max
5. **Win/Loss Conditions**:
   - Win: All letters revealed before 6 failed attempts
   - Loss: 6 failed attempts reached

## Implementation Patterns

### Input Validation Pattern
- Use `try...except` for error handling on invalid inputs
- Validate: single character only, alphabetic only, not previously guessed
- Reject duplicates by maintaining a guessed letters set
- Provide clear feedback for each rejection type

### Game State Management
- Track current display state (dashes for unguessed, letters for guessed)
- Maintain failed attempt count
- Store guessed letters set for duplicate prevention
- Update display dynamically as correct letters are revealed

### Word Display Logic
- Initialize word as all dashes: `'-' * len(word)`
- Replace dashes with letters: convert to list, update positions, rejoin
- Example: word="cat", guessed=['c','a'] → "c-a-" becomes "ca-"

## Testing & Execution
- Run directly: `python hangman.py`
- No external dependencies required (uses only `random` built-in)
- Optional enhancement: Python Turtle library for visual hangman drawing (scope extension only)

## Key Files
- `hangman.py`: Main game implementation

## Conventions
- Use descriptive variable names (e.g., `guessed_letters`, `failed_attempts`, `display_word`)
- Keep game loop simple and readable with clear state transitions
- Print user-friendly prompts and feedback messages
- Use string methods (`.lower()`, `.isalpha()`) for input normalization
