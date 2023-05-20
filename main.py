# Welcome User to Hangman Game
import pyfiglet
import random
import sys
import os

from ListOfWords import word_list
from HangmanStages import stages

def gameOver():
    print("Game Over!")

def endGame():
    print("Thanks for Playing!!")
    sys.exit()

def gameClear():
    print("Congratulations!! You Win!!")
    playAgain()

def playAgain():
    replay = input("Would you like to play again? [y/n] ")
    if replay == 'y':
        startGame()
    elif replay == 'n':
        endGame()

def welcomePlayer():
    ascii_banner = pyfiglet.figlet_format("Welcome to Hangman!")
    print(ascii_banner)

    


def startGame():
    wrong_guesses = 6
    rand_word = random.choice(word_list)
    board = []
    for letter in rand_word:
        board.append('-')
    print(board)
    
    while '-' in board:
        player_guess = input('Please guess a letter: ')
        if len(player_guess) == 1:
            occurences = rand_word.count(player_guess)
            indices = [i for i, a in enumerate(rand_word) if a == player_guess]
            if not indices:
                print("Not Found!")
                wrong_guesses = wrong_guesses - 1
                print(stages[wrong_guesses])
                if wrong_guesses == 0:
                    print("The word was: " + rand_word)
                    gameOver()
                    playAgain()
                else:
                    print("Number of guesses remaining: " + str(wrong_guesses))
                    continue

            else:        
                print("Letter Found!")
                for p in indices:
                    board[p] = player_guess
                print(board)
                if '-' not in board:
                    gameClear()
                else:
                    continue
        else:
            print('Enter a single character to continue.')
            continue


welcomePlayer()
startGame()