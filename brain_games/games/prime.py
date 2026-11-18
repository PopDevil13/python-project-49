import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    answer = 'yes'
    question = random.randint(1, 100)
    if question == 1:
        answer = 'no'
    for i in range(2, question):
        if question % i == 0:
            answer = 'no'
    return question, answer

