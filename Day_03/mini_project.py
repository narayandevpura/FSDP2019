# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:30:17 2019

@author: Narayan Devpura
"""

# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""

"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

"""
Challenge 3
Read the words from a file

"""

"""
Challenge 4
    Get the list of Internet after web scrapping
"""


import random
fruits_list = ['apple','banana','mango','grapes','papaya','orange']

pick = random.choice(fruits_list)

chances  = len(fruits_list)/2
left = chances
flag = True
while chances != 0:
    if flag:
        guess = input('You have {0} chances....Guess the friut: '.format(chances))
    else:
        guess = input('You guessed wrong...You left with {0} chances....Guess again: '.format(chances))

    if guess == pick:
        chances -= 1
        if chances == (len(fruits_list)/2 - 1) :
            print('Hurray!!! You win in single move...')
            flag = True
            break
        else:
            print("Hurray!!! You guessed the fruit in {0} moves".format(left - chances))
            flag = True
            break
    else:
        chances -= 1
        flag = False
        continue

if not flag:
    print('You ran out of moves!!!   Computer Wins!!!   Better luck next time')
    

    