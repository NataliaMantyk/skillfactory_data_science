import numpy as np

""" Game 'Guess the number' """
""" Computer hides the number and guesses the number for less than 20 attemps """
 
def random_predict_20(number:int=1) -> int:
    
    """Randomly guessing the number for less than 20 attempts
    Args:
        number (int, optional): Hidden number. Defaults to 1.
    Returns:
        int: Number of attempts
    """
    count = 0
    min = 1
    max = 101
    predict = (min + max)//2
    
    while number != predict:
        count += 1
        if number > predict:
            min = predict + 1
        else:
            max = predict -1
        predict = (min + max)//2
    return count

def score_game_20(random_predict_20) -> int:
    
    """For how many attempts in average within 1.000 approaches the number would be guessed.
    
    np.random.see(1) - The random number generator needs a number to start with (a seed value), to be able to generate a random number.
    
    Args:
        random_predict() - guess function
    Returns:
        int: average number of attempts"""
        
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_list.append(random_predict_20(number))
    
    score = int(np.mean(count_list))
    
    print(f'Your algorithm is guessing the number for {score} attempts')
    
    return score

if __name__ == "__main__":
    score_game_20(random_predict_20)