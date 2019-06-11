"""Import random functions from Python library"""
import re
import random
"""Import Regular Expressions from Python library"""


source_words = open("words.txt").read()
source_words = source_words.lower().split()

# num_of_words = len(source_words)
computer_picked_word = source_words
allowed_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()


easy_word_list = []


def easy_words(source_words):
    for word in source_words:
        if len(word) >= 1 and len(word) <= 5:
            easy_word_list.append(word)
    return easy_word_list


easy_words(source_words)
# print(easy_word_list)

medium_word_list = []


def medium_words(source_words):
    for word in source_words:
        if len(word) >= 6 and len(word) <= 7:
            medium_word_list.append(word)
    return medium_word_list


medium_words(source_words)
# print(medium_word_list)

hard_word_list = []


def hard_words(source_words):
    for word in source_words:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list


hard_words(source_words)
# print(hard_word_list)


def greeting():
    print("Welcome to Mystery Word Game!!")
    print("Try to guess the word in 8 tries or less")
    print("**********************************************************")


greeting()


def start_of_game():
    level_choice = int(input(
        "What level would you like to play? Please enter 1-Easy, 2-Medium, 3-Hard. "))
    if level_choice == 1:
        computer_picked_word = random.choice(easy_word_list)
        
        print("Your word is ", len(computer_picked_word), "letters")

    elif level_choice == 2:
        computer_picked_word = random.choice(medium_word_list)
        print("Your word is ", len(computer_picked_word), "letters")
    
    elif level_choice == 3:
        computer_picked_word = random.choice(hard_word_list)
            
        print("Your word is ", len(computer_picked_word), "letters")

    return computer_picked_word


computer_picked_word = start_of_game()

def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    correct_word = random.choice(source_words)
    return correct_word
random_word(source_words)

guesses = []
#count = 0
guess_limit = 8
out_of_guesses = False
correct_word = computer_picked_word



def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"


def game_play(out_of_guesses):
    count = 0
    print(correct_word)
    while not out_of_guesses:
        guess_input = str(input("Please guess a letter: " ))
        if guess_input in correct_word:
            guesses.append(guess_input)
            display_letters = [display_letter(letter, guesses) for letter in correct_word]
            print('correct')
            display_letters = ''.join(display_letters)
            print(display_letters)
            if display_letters == correct_word:
                
                print("You Win")
                return
        elif count < guess_limit -1:
            count+=1
            print("You have used " + str(count))
        else:
            out_of_guesses = True

game_play(out_of_guesses)
