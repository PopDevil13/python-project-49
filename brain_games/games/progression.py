import random

DESCRIPTION = 'What number is missing in the progression?'


def arif_listing():
    start = random.randint(3, 20)
    step = random.randint(2, 10)
    count = 10
    stop = start + (step * count)
    progression = list(range(start, stop, step))
    return progression


def get_question_and_answer():
    progression = arif_listing()
    random_index = random.randint(2, len(progression) - 1)

    answer = str(progression[random_index])
    progression[random_index] = ".."
    question = " ".join(str(num) for num in progression)
    return question, answer

       
