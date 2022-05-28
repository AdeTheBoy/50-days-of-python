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
    while no_of_lives > 0:
        guess = int(input("Guess a number: "))
        if guess > rand_number:
            no_of_lives -= 1
            print(f"Too high!\nYou have {no_of_lives} left.")
        elif guess < rand_number:
            no_of_lives -= 1
            print(f"Too Low!\nYou have {no_of_lives} left.")
        elif guess == rand_number:
            no_of_lives -= no_of_lives

    if guess == rand_number:
        print("You Win!")
    else:
        print("You Lose :(")
    game_end = True
    
