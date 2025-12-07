import random

# Word list for the game
hangman_words = [
    "python", "hangman", "computer", "programming", "developer",
    "algorithm", "function", "variable", "database", "network",
    "internet", "software", "hardware", "keyboard", "monitor"
]
# Helper functions
def get_display_word(word, guessed_letters):
    """Return the word with unguessed letters as dashes."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display
#
def is_valid_guess(guess, guessed_letters):
    """Validate that the guess is a single, alphabetic, unguessed letter."""
    if len(guess) != 1:
        print("Please enter only one letter.")
        return False
    if not guess.isalpha():
        print(" Please enter a letter (a-z).")
        return False
    if guess in guessed_letters:
        print(f" You already guessed '{guess}'. Try another letter.")
        return False
    return True

def play_hangman():
    """Main game loop for Hangman."""
    word = random.choice(hangman_words).lower()
    guessed_letters = set()
    failed_attempts = 0
    max_attempts = 6
    
    print("=" * 50)
    print(" Welcome to Hangman!")
    print("=" * 50)
    print(f"I'm thinking of a word with {len(word)} letters.")
    print(f"You have {max_attempts} failed attempts to guess it.\n")
    
    while failed_attempts < max_attempts:
        # Display current state
        display_word = get_display_word(word, guessed_letters)
        print(f"\nWord: {display_word}")
        print(f"Failed attempts: {failed_attempts}/{max_attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if player won
        if display_word == word:
            print("\n" + "=" * 50)
            print(f" You Won! The word was: {word}")
            print("=" * 50)
            return
        
        # Get player guess
        try:
            guess = input("\nGuess a letter: ").lower()
        except EOFError:
            print("\nGame ended.")
            return
        
        # Validate guess
        if not is_valid_guess(guess, guessed_letters):
            continue
        
        # Process guess
        guessed_letters.add(guess)
        if guess in word:
            print(f" Good guess! '{guess}' is in the word.")
        else:
            failed_attempts += 1
            print(f" Sorry, '{guess}' is not in the word.")
    
    # Game over - player lost
    print("\n" + "=" * 50)
    print(f" Game Over! You Lost!")
    print(f"The word was: {word}")
    print("=" * 50)

if __name__ == "__main__":
    play_hangman()


