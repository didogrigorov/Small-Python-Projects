import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names)

random_choice = random.randint(0, length - 1)
payee = names[random_choice]
print(payee)
