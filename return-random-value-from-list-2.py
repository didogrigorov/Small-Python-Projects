import random

number = int(input("enter how many numbers "))
l = [0, 1, 2, 3, 4]

for item in range(1, number+1):

  print(random.choice(l), end=" ")
