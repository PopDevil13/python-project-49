from brain_games.cli import welcome_user
import random
import math
def brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    win_counter = 0
    while win_counter < 3:
        a = random.randint(1,100)
        b = random.randint(1,100)
        gcd = math.gcd(a, b)
        print(f'Question:', a, b)
        user_answer = int(input())
        correct_answer = gcd
        if user_answer == correct_answer:
            win_counter += 1
            user_answer == a
            print('Correct!')
        else:
            print(f"'{user_answer}',is wrong answer ;(. Correct answer was, '{correct_answer}'")
            return
    print(f"Congratulations, {name}!")