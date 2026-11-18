import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f'{a} {b}'
    answer = str(math.gcd(a, b))
    return question, answer 
