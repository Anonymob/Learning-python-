import random
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock ='''
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

rock_list = [rock,paper,scissor]
c_no = random.randint(0,2)
computer_move= rock_list[c_no]
human_move = rock_list[int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]

print(computer_move)
print(human_move)

if computer_move == human_move:
    print("draw")
elif computer_move == paper and human_move == scissor:
    print("you win")
elif computer_move == rock and human_move == paper:
    print("you win")
elif computer_move == scissor and human_move == rock:
    print("you win")
else:
    print("you lose")