import numpy as np

""" Game 'Guess the number' """
""" Computer hides the number and guess the number for less than 20 attempts """
""" Below two algorithms are presented"""

np.random.seed(1)
random_array = np.random.randint(1, 508, size=(1000))
count_list = []

""" Option 1: Binary approach has been used"""

def game_core(number):
    count = 0
    min = 1
    max = 508
    predict = (min + max)//2
    while number != predict:
        count +=1
        if number > predict: 
            min = predict + 1
        else:
            max = predict - 1
        predict = (min+max)//2    
    return count

""" Algorithm verification / examination """

for number in random_array:
    count_list.append(game_core(number))
print(np.mean(count_list))

""" Option 2: Aproach via step element usage """

def game_score(number, step=10):
    count = 0
    predict = 0
    while number != predict:
        count += 1
        if number > predict:
            predict += step
        else:
            predict -= 1
    return count
    
""" Algorithm verification / examination """
for number in random_array:
    count_list.append(game_score(number))
print(int(np.mean(count_list)))

if __name__ == " __main__":
    game_core(number)
    
if __name__ == " __main__ ":
    game_score(number)