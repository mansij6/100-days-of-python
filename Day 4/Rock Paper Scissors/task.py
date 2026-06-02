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
user_choice = input("what do you choose? type 0 gor rock,"
                    "1 for paper, or 2 for scissors:\n ")

computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")
def foo() -> str:
    return "abc"

a: str
a = foo()
if user_choice >= 3 or computer_choice < 0: #expected type 'str', got 'int' instead
    print("you typed an invalid number. you lose!")


if user_choice == 0 and 2 == computer_choice:
    print("you wins!")
elif computer_choice == 0 and 2 == computer_choice:
    print("you lose!")
elif  computer_choice > user_choice:
    print("you lose!")
elif computer_choice > user_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw!")


