from brain_games.cli import welcome_user
import random
def brain_prime():
    name = welcome_user()
    win_counter = 0
    while win_counter < 3:
        prime = True
        random_number = random.randint(1, 100)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print(f'Question:', random_number)
        if random_number == 1: 
            prime = False
        for i in range(2, random_number):
            if random_number % i == 0:
                prime = False
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if prime == True else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            win_counter += 1
        else:
            print(f"'{user_answer}',is wrong answer ;(. Correct answer was, '{correct_answer}'")
            return


    
