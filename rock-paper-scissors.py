import random 

rock = '''
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
game_images  = [rock,paper,scissors]
user_action = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You chose:" + game_images[user_action])

computer_action = random.randint(0,2)
print("Computer chose:" + game_images[computer_action])

if user_action > computer_action:
  print("You win")
elif user_action < computer_action:
  print("You lose")
elif user_action == computer_action:
  print("It's a draw!")
else:
  print("You typed a wrong number!Try again!")
