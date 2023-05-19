# Welcome User to Hangman Game
import pyfiglet
import random
import sys
import os

from ListOfWords import word_list
from HangmanStages import stages

def gameOver():
    print("Game Over!")
    sys.exit()

def gameClear():
    print("Congratulations!! You Win!!")
    playAgain()

def playAgain():
    replay = input("Would you like to play again? [y/n] ")
    if replay == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif replay == 'n':
        sys.exit()

ascii_banner = pyfiglet.figlet_format("Welcome to Hangman!")
print(ascii_banner)

wrong_guesses = 6



# Generate random word from list
rand_word = random.choice(word_list)



# Generate number of blank spaces equal to length of random word
board = []
for letter in rand_word:
    board.append('-')
print(board)

# Prompt user to guess one random letter

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
                gameOver()
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
    
    
    



"""     if player_guess in rand_word:
        print("Found the letter!")
        list = findIndex(rand_word, player_guess)
        print(list)
            
    else:
        print("Letter not found..") """






# Reload blank word - inform user of correct guess by making new letter appear in blanks
#                   - inform user of incorrect guess by showing next hangman stage

# After number of incorrect guesses:
    #1. Inform user that game has ended
    #2. Show final hangman stage
    #3. Show full random word to user
    #4. Play again?

# After full word solved:
    #1. Infom user that the game has ended
    #2. Congratulate user on win!
    #3. Show full random word to user
    #4. Play again?