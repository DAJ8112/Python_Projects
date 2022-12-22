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
#0-rock
#1-paper
#2-scissors
#Write your code below this line 👇
user=input("Enter R for Rock, P for Paper, S for Scissors\n")
comp=random.randint(0,2)
if comp==0:
  print("Computer's choice :",rock)
elif comp==1:
  print("Computer's choice :",paper)
elif comp==2:
  print("Computer's choice :",scissors)
if user=='R':
  print("Your choice:",rock)
  if comp==0:
    print("Tie")
  elif comp==1:
    print("You Win !")
  elif comp==2:
    print("You lose !")
    
elif user=='P':
  print("Your choice:",paper)
  if comp==0:
    print("You Win !")
  elif comp==1:
    print("Tie")
  elif comp==2:
    print("You lose !")
    
elif user=='S':
  print("Your choice:",scissors)
  if comp==0:
    print("You lose !")
  elif comp==1:
    print("You win !")
  elif comp==2:
    print("Tie")
  
    
