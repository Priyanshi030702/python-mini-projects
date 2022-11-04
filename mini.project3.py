import random


user_wins = 0
computer_wins = 0
options  = ['rock','papper','scissors']


while True:
    user_input = input('type Rock/Papper/Scissors or Q to quit').lower()
    if user_input == 'q':
        break
    if user_input not in ['rock','papper','scissors']:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print('computer picks',computer_pick + '.')
    if user_input == 'rock' and computer_pick == 'scissor':
        print('hey you won')
        user_wins = user_wins + 1
        
    elif user_input == 'paper' and computer_pick == 'rock':
        print('hey you won')
        user_wins = user_wins + 1
        
    elif user_input == 'scissor' and computer_pick == 'paper':
        print('hey you won')
        user_wins = user_wins + 1
    elif user_input == computer_pick:
        print('no one won')    
    else:
        print('you lost')
        computer_wins = computer_wins +1


