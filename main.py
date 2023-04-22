def run_quiz(quiz: list[dict]):
    score = 0
    for q in quiz:
        print(q["question"])
        for variant, answer in q["options"].items():
            print(f"{variant}) {answer}")
        user_answer = input("Your answer: ")
        if user_answer == q["answer"]:
            score += 1
    return score


import json

with open('quiz.json') as f:
    quiz = json.load(f)

score = run_quiz(quiz)
print(f"Your score is {score}")
user_name = input('Enter your name: ')
score = str(score)
leaderboard = (user_name + ' ' + score)
result_to_save = json.dumps(leaderboard)
with open('leaderboard.json', 'a') as f:
    json.dump(result_to_save, f)