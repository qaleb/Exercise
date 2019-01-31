"""
Word Guess Game

by Coal_
"""
import random

WORDS = ('apple', 'oracle', 'amazon', 'microsoft')
correct_word = random.choice(WORDS)
clue = correct_word[0] + correct_word[-1]

store_letter = ''
limit = 5

print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print('Let\'s begin!')
print()

for guess_count in range(limit):
    while True:
        letter_guess = input('Guess a letter: ')

        if len(letter_guess) == 1:
            break
        else:
            print("Oops! Guess a letter!")

    if letter_guess in correct_word:
        print('yes!')
        store_letter += letter_guess
    else:
        print('no!')

    if guess_count == 2:
        print()
        clue_request = input('Would you like a clue?')
        if clue_request.lower().startswith('y'):
            print()
            print('CLUE: The first and last letter of the word is: ', clue)
        else:
            print('You\'re very brave!')

print()
print('Now its time to guess. You have guessed', len(store_letter), 'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')
if word_guess.lower() == correct_word:
    print('Congrats!')
else:
    print('Unlucky! The answer was,', correct_word)

print()
input('Press Enter to leave the program')