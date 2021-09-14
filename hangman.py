import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives>0:
        print('You have used letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-'  for letter in word]
        print('Current Word: ', ' '.join(word_list))

        # get user input
        user_letter = input("Guess the letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            lives -= 1
            print('You already used that character.Try again!!\nLives remaining: ', lives)

        else:
            print('Invalid character.Try again!')

    if lives>0:
        print(f'You Won!!\nWord: {word}')
    
    else:
        print(f'You died!!\nOriginal Word was: {word}')


if __name__=='__main__':
    hangman()