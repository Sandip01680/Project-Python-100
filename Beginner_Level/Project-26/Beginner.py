# Simple Quiz Game

questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter",
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", answer)

print("Your final score is:", score, "out of", len(questions))
