import numpy as np

""" Game 'Guess the number' """
""" Computer hides the number and guesses the number itself"""

def random_predict(number:int = 1) -> int:
    
    """Randomly guessing the number
    Args:
        number (int, optional): Hidden number. Defaults to 1.
    Return:
        int: Number of attempts
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #randomly hidden number
        
        if number == predict_number:
            break #exit the loop if the number have been guessed
    return count
print(f'Number of attempts: {random_predict()}')

def score_game(random_predict) -> int:
    
    """For how many attempts in average within 1.000 approaches the number would be guessed.
    
    np.random.see(1) - The random number generator needs a number to start with (a seed value), to be able to generate a random number.
    
    Args:
        random_predict() - guess function
    Returns:
        int: average number of attempts"""
        
    count_list = [] # empty list to save number of attempts
    np.random.seed(1) # setting the number to start random generating
    random_array = np.random.randint(1, 101, size=(1000)) # have set the list of numbers
        
    for number in random_array:
        count_list.append(random_predict(number))
    
    score = int(np.mean(count_list))
        
    print(f'Your algorithm is guessing the number for {score} attempts')
    return score
score_game(random_predict)

if __name__ == "__main__":
    score_game(random_predict)
    
    
    