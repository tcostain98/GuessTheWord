import json
from random import randrange

lives = 10
guesses = []
done = False
masked_word = ''
current_word = ''

def game_result(user_won, word):
    if user_won:
        print(f"Excellent!, you have won!  The word was {word}!")
    else:
        print(f"So Close!  Better luck next time.  The word was {word}")

def mask_current_word(word):
    masked = []
    for letter in word:
        masked.append('_')
    return ''.join(masked)

def mask_current_word(word):
    masked = []
    for letter in word:
        masked.append('_')
    return ''.join(masked)


def validate_letter_in_word(letter, word):
    return letter.lower() in word.lower()


def get_letter_guess():
    retry_input_guess = True
    guess_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while retry_input_guess:
        letter = input(f"Whats your guess?: ")
        if letter.upper() in guess_options:
            if letter.upper() in guesses:
                print("You have already tried that letter. Have another go.")
            else:
                retry_input_guess = False
        else:
            print('You must enter an alphabetic character.')
    return letter

