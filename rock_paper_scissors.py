import random

pc_points = 0
user_points = 0
draw = 0
rounds = int(input("Choose number of rounds: "))
round_counter = 0

choice = ['rock', 'paper', 'scissor']
for i in range(rounds):
    round_counter += 1
    pc_choice = random.choice(choice)
    user_choice = input(f"Round {round_counter}\nChoose from 'rock','paper','scissor': ")

    if user_choice == 'rock' and pc_choice == 'scissor':
        user_points += 1
    elif user_choice == 'paper' and pc_choice == 'rock':
        user_points += 1
    elif user_choice == 'scissor' and pc_choice == 'paper':
        user_points += 1

    elif pc_choice == 'rock' and user_choice == 'scissor':
        pc_points += 1
    elif pc_choice == 'paper' and user_choice == 'rock':
        pc_points += 1
    elif pc_choice == 'scissor' and user_choice == 'paper':
        pc_points += 1

    print(f"PC choice is: {pc_choice}\nUser score: {user_points} - PC score: {pc_points}")
    if user_choice == pc_choice:
        draw += 1
        print("Round is Tie !")
    print()


if pc_points > user_points:
    print('PC is the winner !')
elif pc_points < user_points:
    print('User is the winner !')
elif pc_points == user_points:
    print('Tie !')
