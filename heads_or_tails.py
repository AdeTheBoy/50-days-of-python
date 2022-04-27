import random
#built in python module


seed = random.randint(1,2)


outcome = random.random() * seed

if outcome < 1:
  print("Heads")
else:
  print("Tails")
  




