def prime_checker(number):
  n = number
  g = 0
  while n > 0: 
    if number % n == 0:
      g += 1
    n -= 1
  if g > 2:
    print("Not a prime")
  else:
    print("Prime number")




    
n = int(input("Check this number: "))
prime_checker(number=n)



