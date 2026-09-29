from brain_games.cli import welcome_user
import random
def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    operators = ['+', '-', '*']
    win_counter = 0
    while win_counter < 3:
        a = random.randint(1,100)
        b = random.randint(1,100)
        question = (f'{a} {random.choice(operators)} {b}')
        answer = str(eval(question))
        print(question)
        user_answer = input()
        if user_answer == answer:
                win_counter += 1
                print('Correct!')
        else:
            print(f"'{user_answer}',is wrong answer ;(. Correct answer was, '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    