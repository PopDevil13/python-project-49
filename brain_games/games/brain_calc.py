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
        random_op = random.choice(operators)
        if random_op == '+':
             expr = a + b
        elif random_op == '-':
             expr = a - b
        elif random_op == '*':
             expr = a * b
        question = (f'{a} {random_op} {b}')
        
        print(question)
        answer = str(expr)
        user_answer = str(input("Your answer: "))
        if user_answer == answer:
                win_counter += 1
                print('Correct!')
        else:
            print(f"'{user_answer}',is wrong answer ;(. Correct answer was, '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    