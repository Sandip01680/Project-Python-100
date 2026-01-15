"""
Interactive Quiz Application
A simple command-line quiz game that tests your knowledge on various topics.
"""

# Constants
PASS_THRESHOLD = 50  # Minimum percentage to pass
VALID_ANSWERS = ["A", "B", "C", "D"]

# Quiz questions database
quiz = [
    {"question": "What is the capital of India?",
     "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
     "answer": "A"},
    
    {"question": "Which language is used for web development?",
     "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
     "answer": "B"},
    
    {"question": "Who developed Python?",
     "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
     "answer": "B"},
    
    {"question": "Which data structure uses key-value pairs?",
     "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
     "answer": "C"},
    
    {"question": "Which planet is known as the Red Planet?",
     "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
     "answer": "B"},
    
    {"question": "What is the largest ocean on Earth?",
     "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
     "answer": "C"},
    
    {"question": "Which device is used to measure temperature?",
     "options": ["A. Barometer", "B. Thermometer", "C. Hygrometer", "D. Altimeter"],
     "answer": "B"},
    
    {"question": "Which symbol is used to comment in Python?",
     "options": ["A. //", "B. #", "C. <!-- -->", "D. %"],
     "answer": "B"},
    
    {"question": "Which keyword is used to define a function in Python?",
     "options": ["A. func", "B. def", "C. function", "D. define"],
     "answer": "B"},
    
    {"question": "Which Excel feature is used to summarize data?",
     "options": ["A. Pivot Table", "B. VLOOKUP", "C. Conditional Formatting", "D. Charts"],
     "answer": "A"}
]


def ask_question(question_data, question_number):
    """
    Display a question and get user's answer.
    
    Args:
        question_data (dict): Dictionary containing question, options, and answer
        question_number (int): The question number to display
        
    Returns:
        int: 1 if answer is correct, 0 if incorrect
    """
    print(f"\nQuestion {question_number}: {question_data['question']}")
    print("\n".join(question_data["options"]))
    
    while True:
        try:
            user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            if user_answer in VALID_ANSWERS:
                break
            print("⚠️ Invalid choice! Please enter A, B, C, or D.")
        except (EOFError, KeyboardInterrupt):
            print("\n\nQuiz interrupted by user. Exiting...")
            return None
    
    if user_answer == question_data["answer"]:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! Correct answer is {question_data['answer']}")
        return 0


def run_quiz(quiz_data):
    """
    Execute the quiz and calculate final score.
    
    Args:
        quiz_data (list): List of question dictionaries
    """
    print("*" * 60)
    print("🎓 Welcome to the Interactive Quiz!")
    print("*" * 60)
    
    score = 0
    total_questions = len(quiz_data)
    
    for index, question in enumerate(quiz_data, start=1):
        result = ask_question(question, index)
        if result is None:  # User interrupted the quiz
            return
        score += result
    
    # Calculate and display results
    total = len(quiz_data)
    percentage = (score / total) * 100
    
    print("\n" + "=" * 60)
    print("🎯 Quiz Completed!")
    print("=" * 60)
    print(f"Your final score: {score}/{total} ({percentage:.2f}%)")
    
    if percentage >= PASS_THRESHOLD:
        print("🏆 Result: PASS")
    else:
        print("❌ Result: FAIL")
    print("=" * 60)


def main():
    """Main function to run the quiz application."""
    try:
        run_quiz(quiz)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again later.")


if __name__ == "__main__":
    main()