import numpy as np
""" 'Game Guess the number' """
    
number = np.random.randint(1, 101) # Think of the number
count = 0 # argument to count number of attempts

while True:
    count += 1
    predict_number = int(input('Guess the number bewtween 1 and 100'))
    if predict_number > number:
        print('The number shall be smaller!')
    elif predict_number < number:
        print('The number shall be bigger!')
    else:
        print(f'You have guessed the number! This number is {number} for {count} number of attempts')
        break
    