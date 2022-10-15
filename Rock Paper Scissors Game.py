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

#Write your code below this line 👇
import random
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

game_images = [rock,paper,scissors]

if (choose > 2 or choose < 0):
  print("Invalid Error'")
  
else:
  print("Your chose :")
  print(game_images[choose])

  random_computer = random.randint(0,2)
  print("Computer chose :")
  print(game_images[random_computer])
  
  if ((choose > random_computer) or (choose == 0 and random_computer == 2)):
    print("You win!")
    
  elif ((choose < random_computer) or (choose == 2 and random_computer == 0)):
    print("You lose!")
  
  else:
    print("You draw!")

  
  