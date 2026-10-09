#надо сгенерировать список числовой прогрессии
#берем из библы рандом функию 
#выставляем переменные с рандомными значениями для списка
#
from brain_games.cli import welcome_user
import random
def arif_listing():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    count = 10
    stop = start + (step*count)
    progression = list(range(start, stop, step)) 
    return progression

def brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    win_counter = 0
    while win_counter < 3:
        current_list = arif_listing()
        random_index = random.randint(0, len(current_list)-1)
        hidden_element = current_list[random_index]
        current_list[random_index] = '..'
        print(f'Question:', *current_list)
        user_answer = int(input('Your answer: '))
        if user_answer == hidden_element:
            win_counter += 1
            print('Correct!')
        else:
             print(f"'{user_answer}',is wrong answer ;(. Correct answer was, '{hidden_element}'")
             return
            
    print(f"Congratulations, {name}!")
    
