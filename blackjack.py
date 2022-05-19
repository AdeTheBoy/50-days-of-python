from art import logo
from replit import clear
import random

"""This function asks a player if they want to start a
new game of blackjack "y" == yes and "n" == no """
def game_start():
  start = input("Would you like to play a game of blackjack? y/n: ")
  
  if start == "y":
      clear()
      return False
  else:
      print("Goodbye!")
      return True
      
"""This function returns a list containing a random 
card from a deck of cards"""
def draw_one():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selection = random.choice(deck)
    return selection

"""This function returns the sum of cards, and returns
0 if the sum is equal to 21"""
def calc_score(cards):
    if sum(cards) == 21 & len(cards) == 2:
        return 0
    else:
        return sum(cards)

"""This function prints the final score and returns True
in order to end the game"""
def final():
    print("You win")
    return True 

game_over = game_start()

while not game_over:
    print(logo)
    print("Welcome to blackjack by Ade :)")
    your_cards = []
    comp_cards = []
    for _ in range(2):
        your_cards.append(draw_one())
        comp_cards.append(draw_one())
    print(f"Your cards are: {your_cards}")
    print(f"The dealer's first card is {comp_cards[0]}")
    if sum(your_cards) == 21 & len(your_cards) == 2:
        final()
    game_over = final()
 
