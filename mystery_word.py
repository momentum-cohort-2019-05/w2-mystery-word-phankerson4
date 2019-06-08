"""Import random functions from Python library"""
import random
"""Import Regular Expressions from Python library""" 
import re 


source_words = open("words.txt").read()
source_words = source_words.lower().split()
num_of_words = len(source_words)




easy_word_list = []
def easy_words(source_words):
    for word in source_words:
        if len(word) >= 1 and len(word) <= 5:
            easy_word_list.append(word)
    return easy_word_list
easy_words(source_words)
#print(easy_word_list)

medium_word_list = []
def medium_words(source_words):
    for word in source_words:
        if len(word) >= 6 and len(word) <= 7:
            medium_word_list.append(word)
    return medium_word_list
medium_words(source_words)
#print(medium_word_list)

def greeting():
    print("Welcome to Mystery Word Game!!")
    level_choice = int(input("What level would you like to play? Please enter 1-Easy, 2-Medium, 3- Hard. "))
    
            
greeting()

        


    #print("The word contains" x amount of letters)


hard_word_list = []
def hard_words(source_words):
    for word in source_words:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list
hard_words(source_words)
#print(hard_word_list)

