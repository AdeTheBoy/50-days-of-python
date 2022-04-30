#This is a band name generator with a twist,
 The twist being if the last and first letter of the first and secondf entries match, the band name is conactenated without a space

print("Welcome to band-name generator 2.0!!!")
# Generates a band name using user inputs: city and pet Name

# User inputs city
x = input("Input the city you grew up in: ")

# User inputs pet name
y = input("Input the name of a pet you've had: ")

# Concatenates if pet name starts with last letter in city, else returns hyphenated band name
if y.startswith(x[-1]) or y.lower()[0] == x[-1]:
   print(x + y[1:-1])
else:
   print(x + "-" + y)
