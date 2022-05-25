#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

def calc_lives():
    chosen = False
    while not chosen:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            chosen = True
            return 10
        elif difficulty == 'hard':
            chosen = True
            return 5
        else:
            print("Wrong input")
            chosen = False

def guessing():
    print
    
print(logo)
game_end = False
while not game_end:
    rand_number = random.randint(1,100)
    print(
f"""Welcome To The Number Guessing Game!
I'm thinking of a number between 1 and 100.
Psst the correct answer is {rand_number}"""
    )
    no_of_lives = calc_lives()
    print(f"You have {no_of_lives} attempts to guess the number.")
    
    game_end = True
    
