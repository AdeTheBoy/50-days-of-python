isrock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

comp_choice = int(random.random() * random.randint(1,3))

choices = [rock, scissors, paper]

print(f'''
      You played
      {choices[choice]}''')

print(f'''
      Computer played
      {choices[comp_choice]}''')

if choice == comp_choice:
  print("It's a draw!")
elif (choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice ==0) or (choice == 2 and comp_choice == 1):
 print("You win!")
else:
 print("Sorry, you lose :(")
