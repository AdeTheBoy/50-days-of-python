from art import logo
from replit import clear
import random

"""This function returns a list containing a random 
card from a deck of cards"""
def draw_one():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selection = random.choice(deck)
    return selection

"""This function returns the sum of cards, or returns
0 if the sum is equal to 21"""
def check_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    elif sum(cards) == 21:
        return 0
    else:
        return sum(cards)

def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went Over, you lose!"
    if user_score == comp_score:
        return "Draw!"
    elif comp_score == 0:
        return "Computer wins with a Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went Over, you lose!"
    elif comp_score > 21:
        return "Opponent went Over, you win!"  
    elif user_score > comp_score:
        return "You win!"
    else:
        return "You lose"

"""This function asks the player if they would like another card, and deals one if they want one"""
def hit(cards):
    one_more = input("Would you like another card? y/n: ")
    if one_more == "y":
        cards.append(draw_one())
        check_score(cards)
        print(f"Your cards are: {cards}")
        print(f"Your total is: {sum(cards)}")
        if sum(cards) == 21 or sum(cards) > 21:
            return
        else:
            hit(cards)
    else:
        return 

def final(your_cards, comp_cards):
    print()

def play_game():
    print(logo)
    print("Welcome to blackjack by Ade :)")
    your_cards = []
    comp_cards = [] 
    for _ in range(2):
        your_cards.append(draw_one())
        comp_cards.append(draw_one())
    print(f"Your cards are: {your_cards}")
    print(f"Your total is: {sum(your_cards)}")
    print(f"The dealer's first card is {comp_cards[0]}")
    total = sum(your_cards)
    if total == 21 or total > 21:
        ()
    else:
        hit(your_cards)
    while sum(comp_cards) < 17 :
        comp_cards.append(draw_one())
    user_score = check_score(your_cards)
    comp_score = check_score(comp_cards)
    print(f"Dealer's cards are: {comp_cards}")
    print(f"Dealer's total is: {sum(comp_cards)}")
    print(compare(user_score,comp_score))

game_stop = False
"""This asks a player if they want to start a
new game of blackjack "y" == yes and "n" == no """
while not game_stop:
    start = input("Would you like to play a game of blackjack? y/n: ")
    if start == "y":
        clear()
        play_game()
        game_stop = False
    else:
        print("Goodbye!")
        game_stop = True
