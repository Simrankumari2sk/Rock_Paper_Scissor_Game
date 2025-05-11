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

user = int(input("What do you choose to play with the computer ? Select 0 for Rock, 1 for Paper and 2 for scissors"))
print("You")
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

print("Computer:")
computer = (rock, paper, scissors)
random_computer = random.randint(a=0, b=2)
print(computer[random_computer])

if user == random_computer:
    print("It's a Draw")
elif user == 0 and random_computer == 1:
    print("OOPS! You Lose")
elif user == 0 and random_computer == 2:
    print("Hurrayyy! You have won the game")
elif user == 1 and random_computer == 0:
    print("Hurrayy! You have won the game")
elif user == 1 and random_computer == 2:
    print("OPPS! You Lose")
elif user == 2 and random_computer == 0:
    print("OOPS! You lose")
elif user == 2 and random_computer == 1:
    print("Hurrayyy! You have won the game")
else:
    print("You put an invalid element")