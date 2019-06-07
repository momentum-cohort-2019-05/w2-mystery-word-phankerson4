"""Import random functions from Python library"""
import random
"""Import Regular Expressions from Python library""" 
import re 
"""Open words.txt file"""
source_words= open("words.txt", "r")
"""Read the lines in the word.txt file"""
words = (source_words.readlines())
"""Create variable and assign it random words"""
computer_generated_random_word = random.choice(words)


def greeting():
    print("Welcome to Mystery Word Game!!")
    level_choice = input("What level would you like to play? Please enter easy, medium, or hard. ")
    level_choice = level_choice.lower()
    #if level_choice == "easy":

    #print("The word contains" x amount of letters)
greeting()

    

