from brain_games.cli import welcome_user
import random
def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win_counter = 0
    correct_answer = ''
    while win_counter < 3:
        random_number = random.randint(1, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        print("Question:", random_number)
        user_answer = input()
        if user_answer == correct_answer:
           win_counter += 1
        elif user_answer != correct_answer:
           print(f"'{user_answer}',is wrong answer ;(. Correct answer was, '{correct_answer}'")
           return
    
    print('Congratulations,', name)
       
    
    




