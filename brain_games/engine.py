from brain_games.cli import welcome_user

GAME_ROUNDS_COUNT = 3


def run_game(game) -> None:
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, answer = game.get_question_and_answer()
        print("Question:", question)
        user_answer: str = input("Your answer: ")
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'"
                )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")