import random

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operators = ["+", "-", "*"]
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    random_op = random.choice(operators)
    if random_op == "+":
        answer = str(a + b)
        question = (f'{a} + {b}')
    elif random_op == "-":
        answer = str(a - b)
        question = (f'{a} - {b}')
    elif random_op == "*":
        answer = str(a * b)
        question = (f'{a} * {b}')
    return question, answer 
