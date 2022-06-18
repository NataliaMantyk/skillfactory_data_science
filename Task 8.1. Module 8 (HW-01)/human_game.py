"""Game: Guess the number"""

import numpy as np

number = np.random.randint(1, 101) # hiding the number

count = 0 # to count the number of attempts

while True:
    count += 1
    predict_number = int(input("Enter any number between 1 and 100: "))
    
    if predict_number > number:
        print("The number shall be smaller!")
        
    elif predict_number < number:
        print("The number shall be bigger!")
    
    else:
        print(f"You've guessed the number! This number is {number} for {count} attempts")
        break   # end of game and exit from loop
    