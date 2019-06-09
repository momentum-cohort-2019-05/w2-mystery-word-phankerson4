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
            computer_picked_word = easy_word_list
    return computer_picked_word
    print("Your word is ", len(random.choice(easy_word_list)), "letters")
    if level_choice == 2:
            computer_picked_word = medium_word_list
    return computer_picked_word
    print("Your word is ", len(random.choice(medium_word_list)), "letters")
    if level_choice == 3:
            computer_picked_word = hard_word_list
            return computer_picked_word
    print("Your word is ", len(random.choice(hard_word_list)), "letters")

start_of_game()
