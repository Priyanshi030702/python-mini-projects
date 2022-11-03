
import random
top_of_range = input("enter the maximum value: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print('enter the number larger that "0"')
        quit()
else:
    quit()
random_number = random.randint(0,top_of_range)

guess = 0
while True:
    guess = guess + 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print('please type a number next time')
        continue
    if user_guess == random_number:
        print('you got the correct answer')
        break
    else:
        if user_guess< random_number:
            print('u were below number')
        else:
            print('u were above number')
    
print("you got in ",guess , 'guesses')