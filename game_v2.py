import numpy as np
""" Game 'Guess the number'
    Computer think about the number itself and guess it itself"""
def random_predict(number:int = 1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # hidden number
        if number == predict_number:
            break # exit from loop if have guessed the number
    return(count)
print(f'Number of attempts: {random_predict()}')

def score_game(random_predict) -> int:
    """For how many attempts in average within 1000 approaches
    the number would be guessed.
    
    np.random.seed(1) - The random number generator needs a number 
    to start with (a seed value), to be able to generate a random number.

    Args:
        random_predict ([_type_]): guess function

    Returns:
        int: average number of attempts
    """
    count_ls = [] # list to save number of attempts
    np.random.seed(1) # setting the number to start random generating
    random_array = np.random.randint(1, 101, size=(1000)) # have set the list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # average number of attempts
    
    print(f'Your algorithm is guessing the number for {score} attempts in average')
    return (score)
score_game(random_predict)
if __name__ == '__main__':
    score_game(random_predict)
        