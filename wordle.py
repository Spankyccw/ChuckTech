# Title: wordle03.py
# Author: cwilliams
# Date: 07/10/2022 
# Purpose: See game Wordle
# Date/Name/Change

#!\C:\Users\chuck\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts
from colorama import init, Fore, Back, Style
import random
number_of_attempts = 6
init()

loop = True
# ideally pull from a dictionary of 5 letter words
word_list = ["crown", "build", "logic", "plane", "focus", "money", "plant", "plate", "pound", "other", "input", "horse", "green", "group", "beans", "guide", "layer", "mayor", "lunch", "limit", "model", "point", "scope", "score", "title", "total", "world"]
print('')
print('This game is like Wordle. Guess the five letter word in six tries.')
print('Red is correct letter in correct place. Yellow is correct letter in incorrect place.')
while loop:
    print(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit)" + Style.RESET_ALL)
    command = input()
    if command == "quit":
        loop = False
    elif command == "y":
        inner_loop = 0
        word = random.choice(word_list)

        print("Enter your 5 letter word guess:")

        while inner_loop < number_of_attempts:

            while True:
                try:
                    attempt = str(input())
                    attempt_length = len(attempt)
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    #better try again... Return to the start of the loop
                    continue
                #else attempt is None:
                #    print('You must enter a 5 letter word, genius.')
                #    continue
                elsif attempt_length <> 5:
                    print('You must enter a 5 letter word, genius.')
                    continue
                else: 
                    #value acceptable, as far as we can tell
                    break
                
            # Game logic

            output = ""
            
            for i in range(word.__len__()):
                if attempt[i] == word[i]:
                    output = output + Back.RED + attempt[i] + Back.RESET
                elif attempt[i] in word:
                    output = output + Back.YELLOW + attempt[i] + Back.RESET
                else:
                    output = output + attempt[i] + Back.RESET
            print(output)
            if word == attempt:
                print("Congratulations!")
                inner_loop = inner_loop + number_of_attempts # Reset game

            inner_loop = inner_loop + 1
        if word != attempt:
            print('The secret word was', word)