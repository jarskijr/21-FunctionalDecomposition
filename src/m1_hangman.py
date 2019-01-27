"""
Hangman.

Authors: Jacob Jarski and Tim Wilson.
"""  # DONE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
import random
####### Do NOT attempt this assignment before class! #######
def main():
    print('Welcome to Hangman')
    minimum_length = int(input('What is the minimum length you would like your word to be?'))
    item = word_list(minimum_length)
    word_length = length(item)
    repeat( item, word_length)
def word_list(minimum_length):

     with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0, len(words))
        item = words[r]
        while True:
            if len(item) >= minimum_length:
                return item


def length(item):
    spaces = []
    for k in range(len(item)):
           spaces = spaces + ['-']
    return spaces

def guess(item, word_length, guesses):
    letter_guess = str(input('What letter do you want to try?'))
    for k in range(len(item)):
        if letter_guess == item[k]:
            word_length[k] = letter_guess

def clone_original_word_length(word_length, original_word_length):
    for k in range(len(word_length)):
        original_word_length[k] = word_length[k]

def correct_original_word(item):
    correct_original_word=[]
    for k in range(len(item)):
        correct_original_word=correct_original_word+[item[k]]
    return correct_original_word
def play_again():
    response=input('Would you like to play again?(Answer yes or no)')
    if response=='yes':
        main()



def repeat(item, word_length):
    guesses = int(input('Input an amount of wrong guesses allowed.'))
    original_word_length = length(item)


    while True:
        if word_length==correct_original_word(item):
            print('Congratulations')
            play_again()
            break
        elif guesses > 0:
            guess(item, word_length, guesses)
            if original_word_length == word_length:
                guesses = guesses - 1
                print('Incorrect! You still have ', guesses, 'guesses left')
            else:
                clone_original_word_length(word_length, original_word_length)
                print(word_length)
        else:
            print('Sorry you took the L')
            play_again()
            break

















main()