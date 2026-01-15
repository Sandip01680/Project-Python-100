# Advanced Level

import json
import os
import random
from datetime import datetime


# Quiz questions database organized by category
QUIZ_DATABASE = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": 2,
            "difficulty": "easy"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": 1,
            "difficulty": "easy"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "answer": 2,
            "difficulty": "medium"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3,
            "difficulty": "easy"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1943", "1944", "1945", "1946"],
            "answer": 2,
            "difficulty": "medium"
        }
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Go", "Gd", "Au", "Ag"],
            "answer": 2,
            "difficulty": "medium"
        },
        {
            "question": "How many bones are in the adult human body?",
            "options": ["196", "206", "216", "226"],
            "answer": 1,
            "difficulty": "hard"
        },
        {
            "question": "What is the speed of light?",
            "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"],
            "answer": 0,
            "difficulty": "medium"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"],
            "answer": 2,
            "difficulty": "easy"
        },
        {
            "question": "What is H2O commonly known as?",
            "options": ["Hydrogen peroxide", "Water", "Salt", "Sugar"],
            "answer": 1,
            "difficulty": "easy"
        }
    ],
    "Technology": [
        {
            "question": "Who is the founder of Microsoft?",
            "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk"],
            "answer": 1,
            "difficulty": "easy"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Central Processor Update"],
            "answer": 0,
            "difficulty": "easy"
        },
        {
            "question": "What year was the first iPhone released?",
            "options": ["2005", "2006", "2007", "2008"],
            "answer": 2,
            "difficulty": "medium"
        },
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"],
            "answer": 0,
            "difficulty": "easy"
        },
        {
            "question": "Who invented the World Wide Web?",
            "options": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Mark Zuckerberg"],
            "answer": 2,
            "difficulty": "medium"
        }
    ],
    "Sports": [
        {
            "question": "How many players are on a soccer team?",
            "options": ["9", "10", "11", "12"],
            "answer": 2,
            "difficulty": "easy"
        },
        {
            "question": "Which country won the FIFA World Cup 2018?",
            "options": ["Brazil", "Germany", "France", "Argentina"],
            "answer": 2,
            "difficulty": "medium"
        },
        {
            "question": "How many rings are on the Olympic flag?",
            "options": ["4", "5", "6", "7"],
            "answer": 1,
            "difficulty": "easy"
        },
        {
            "question": "What is the diameter of a basketball hoop in inches?",
            "options": ["16", "18", "20", "22"],
            "answer": 1,
            "difficulty": "hard"
        },
        {
            "question": "In which sport would you perform a slam dunk?",
            "options": ["Volleyball", "Tennis", "Basketball", "Baseball"],
            "answer": 2,
            "difficulty": "easy"
        }
    ]
}


class QuizGame:
    """Main quiz game class."""
    
    def __init__(self, leaderboard_file="quiz_leaderboard.json"):
        """Initialize quiz game."""
        self.leaderboard_file = leaderboard_file
        self.leaderboard = self.load_leaderboard()
        self.current_score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.current_streak = 0
        self.best_streak = 0
    
    def load_leaderboard(self):
        """Load leaderboard from file."""
        if os.path.exists(self.leaderboard_file):
            try:
                with open(self.leaderboard_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_leaderboard(self):
        """Save leaderboard to file."""
        try:
            with open(self.leaderboard_file, 'w') as f:
                json.dump(self.leaderboard, f, indent=2)
            return True
        except Exception as e:
            print(f"❌ Error saving leaderboard: {e}")
            return False
    
    def add_to_leaderboard(self, name, score, category, questions_answered):
        """Add score to leaderboard."""
        entry = {
            "name": name,
            "score": score,
            "category": category,
            "questions": questions_answered,
            "accuracy": (self.correct_answers / questions_answered * 100) if questions_answered > 0 else 0,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.leaderboard.append(entry)
        
        # Sort by score (descending)
        self.leaderboard.sort(key=lambda x: x["score"], reverse=True)
        
        # Keep top 10
        self.leaderboard = self.leaderboard[:10]
        
        self.save_leaderboard()
        
        return self.leaderboard.index(entry) + 1 if entry in self.leaderboard else None
    
    def display_leaderboard(self):
        """Display top scores."""
        if not self.leaderboard:
            print("\n🏆 Leaderboard is empty. Be the first to play!")
            return
        
        print("\n" + "=" * 90)
        print("🏆 LEADERBOARD - TOP 10 SCORES")
        print("=" * 90)
        print(f"{'Rank':<6} {'Name':<15} {'Score':<10} {'Category':<20} {'Questions':<12} {'Accuracy':<10} {'Date'}")
        print("-" * 90)
        
        for i, entry in enumerate(self.leaderboard, 1):
            rank_emoji = ["🥇", "🥈", "🥉"][i-1] if i <= 3 else f"{i}."
            print(f"{rank_emoji:<6} {entry['name']:<15} {entry['score']:<10} {entry['category']:<20} "
                  f"{entry['questions']:<12} {entry['accuracy']:.1f}%{' ':<5} {entry['date'][:10]}")
        
        print("=" * 90)
    
    def calculate_score(self, difficulty, time_taken, is_correct):
        """
        Calculate score based on difficulty and time.
        
        Scoring system:
        - Easy: 10 points
        - Medium: 20 points
        - Hard: 30 points
        - Time bonus: Up to 10 extra points (faster = more points)
        - Streak bonus: +5 points per streak
        """
        if not is_correct:
            return 0
        
        # Base score by difficulty
        base_scores = {"easy": 10, "medium": 20, "hard": 30}
        score = base_scores.get(difficulty, 10)
        
        # Time bonus (10 points if answered under 5 seconds)
        if time_taken < 5:
            time_bonus = 10
        elif time_taken < 10:
            time_bonus = 5
        else:
            time_bonus = 0
        
        # Streak bonus
        streak_bonus = min(self.current_streak * 5, 25)  # Max 25 bonus points
        
        return score + time_bonus + streak_bonus
    
    def reset_game(self):
        """Reset game statistics."""
        self.current_score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.current_streak = 0
        self.best_streak = 0
    
    def play_quiz(self, category, num_questions=5, shuffle=True):
        """
        Play a quiz.
        
        Args:
            category: Quiz category
            num_questions: Number of questions
            shuffle: Shuffle questions
        """
        self.reset_game()
        
        # Get questions
        if category == "Mixed":
            all_questions = []
            for cat_questions in QUIZ_DATABASE.values():
                all_questions.extend(cat_questions)
            questions = all_questions
        else:
            questions = QUIZ_DATABASE.get(category, [])
        
        if not questions:
            print(f"❌ No questions available for category: {category}")
            return
        
        # Shuffle and select questions
        if shuffle:
            questions = random.sample(questions, min(num_questions, len(questions)))
        else:
            questions = questions[:num_questions]
        
        self.total_questions = len(questions)
        
        print("\n" + "=" * 80)
        print(f"🎮 QUIZ: {category}")
        print("=" * 80)
        print(f"Questions: {self.total_questions}")
        print(f"Instructions: Select the correct answer (1-4)")
        print("=" * 80)
        
        input("\nPress Enter to start...")
        
        # Ask questions
        for i, q in enumerate(questions, 1):
            print("\n" + "-" * 80)
            print(f"Question {i}/{self.total_questions}")
            print(f"Difficulty: {q['difficulty'].upper()}")
            print("-" * 80)
            print(f"\n{q['question']}")
            print()
            
            # Display options
            for j, option in enumerate(q['options'], 1):
                print(f"  {j}. {option}")
            
            # Start timer
            start_time = datetime.now()
            
            # Get answer
            while True:
                try:
                    answer = input("\nYour answer (1-4): ").strip()
                    answer_idx = int(answer) - 1
                    
                    if 0 <= answer_idx < len(q['options']):
                        break
                    else:
                        print("⚠️  Please enter a number between 1 and 4.")
                except ValueError:
                    print("⚠️  Invalid input. Please enter a number.")
            
            # Calculate time taken
            time_taken = (datetime.now() - start_time).total_seconds()
            
            # Check answer
            is_correct = (answer_idx == q['answer'])
            
            if is_correct:
                self.correct_answers += 1
                self.current_streak += 1
                self.best_streak = max(self.best_streak, self.current_streak)
                
                points = self.calculate_score(q['difficulty'], time_taken, True)
                self.current_score += points
                
                print(f"\n✅ CORRECT! +{points} points")
                
                if self.current_streak > 1:
                    print(f"🔥 Streak: {self.current_streak}!")
            else:
                self.wrong_answers += 1
                self.current_streak = 0
                
                correct_answer = q['options'][q['answer']]
                print(f"\n❌ WRONG!")
                print(f"   Correct answer: {correct_answer}")
            
            print(f"   Time: {time_taken:.1f}s")
            print(f"   Score: {self.current_score}")
        
        # Display results
        self.display_results(category)
    
    def display_results(self, category):
        """Display quiz results."""
        accuracy = (self.correct_answers / self.total_questions * 100) if self.total_questions > 0 else 0
        
        print("\n" + "=" * 80)
        print("📊 QUIZ RESULTS")
        print("=" * 80)
        
        print(f"\n🎯 Performance:")
        print(f"   Total Questions:   {self.total_questions}")
        print(f"   Correct Answers:   {self.correct_answers}")
        print(f"   Wrong Answers:     {self.wrong_answers}")
        print(f"   Accuracy:          {accuracy:.1f}%")
        
        print(f"\n💯 Scoring:")
        print(f"   Final Score:       {self.current_score}")
        print(f"   Best Streak:       {self.best_streak}")
        
        # Performance rating
        if accuracy >= 90:
            rating = "🌟 EXCELLENT! Outstanding performance!"
        elif accuracy >= 75:
            rating = "⭐ GREAT! Well done!"
        elif accuracy >= 60:
            rating = "✨ GOOD! Keep practicing!"
        elif accuracy >= 40:
            rating = "🔰 FAIR! Room for improvement!"
        else:
            rating = "📚 NEEDS WORK! Study more!"
        
        print(f"\n🏆 Rating: {rating}")
        print("=" * 80)
        
        # Add to leaderboard
        if self.current_score > 0:
            name = input("\nEnter your name for the leaderboard: ").strip()
            if name:
                rank = self.add_to_leaderboard(name, self.current_score, category, self.total_questions)
                if rank:
                    print(f"\n🎉 Congratulations! You ranked #{rank} on the leaderboard!")
                else:
                    print(f"\n✓ Score saved! Current score: {self.current_score}")


def display_categories():
    """Display available quiz categories."""
    print("\n" + "=" * 80)
    print("📚 QUIZ CATEGORIES")
    print("=" * 80)
    
    categories = list(QUIZ_DATABASE.keys())
    for i, category in enumerate(categories, 1):
        question_count = len(QUIZ_DATABASE[category])
        print(f"  {i}. {category} ({question_count} questions)")
    
    print(f"  {len(categories) + 1}. Mixed (All categories)")
    print("=" * 80)


def display_rules():
    """Display game rules and scoring system."""
    print("\n" + "=" * 80)
    print("📖 GAME RULES & SCORING")
    print("=" * 80)
    
    print("\n🎯 How to Play:")
    print("  1. Select a quiz category")
    print("  2. Choose number of questions (5-10)")
    print("  3. Answer multiple-choice questions")
    print("  4. Get instant feedback on each answer")
    print("  5. View final score and accuracy")
    
    print("\n💯 Scoring System:")
    print("  • Easy questions:    10 points")
    print("  • Medium questions:  20 points")
    print("  • Hard questions:    30 points")
    
    print("\n⚡ Bonus Points:")
    print("  • Time bonus:        +10 points (under 5 seconds)")
    print("  • Time bonus:        +5 points (5-10 seconds)")
    print("  • Streak bonus:      +5 points per correct in a row")
    print("  • Max streak bonus:  +25 points")
    
    print("\n🏆 Performance Ratings:")
    print("  • 90-100%:  🌟 Excellent")
    print("  • 75-89%:   ⭐ Great")
    print("  • 60-74%:   ✨ Good")
    print("  • 40-59%:   🔰 Fair")
    print("  • 0-39%:    📚 Needs Work")
    
    print("\n🎮 Tips:")
    print("  • Answer quickly for time bonus")
    print("  • Build streaks for extra points")
    print("  • Study categories before playing")
    print("  • Check leaderboard for competition")
    
    print("=" * 80)


def main():
    """Main program execution."""
    game = QuizGame()
    
    print("=" * 80)
    print("                        🎮 SIMPLE QUIZ GAME 🎮")
    print("=" * 80)
    print("\nTest your knowledge across multiple categories!")
    
    while True:
        print("\n" + "-" * 80)
        print("Main Menu:")
        print("  1. Play Quiz")
        print("  2. View Categories")
        print("  3. View Leaderboard")
        print("  4. View Rules & Scoring")
        print("  q. Quit")
        print("-" * 80)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            print("\n🎮 Thanks for playing! See you next time!")
            break
        
        try:
            if choice == '1':
                # Play Quiz
                display_categories()
                
                try:
                    cat_num = int(input("\nSelect category (number): ")) - 1
                    categories = list(QUIZ_DATABASE.keys()) + ["Mixed"]
                    
                    if 0 <= cat_num < len(categories):
                        category = categories[cat_num]
                        
                        # Get number of questions
                        num_q = input("How many questions? (5-10, default 5): ").strip()
                        num_questions = int(num_q) if num_q else 5
                        num_questions = max(5, min(10, num_questions))
                        
                        game.play_quiz(category, num_questions)
                    else:
                        print("❌ Invalid category selection.")
                except ValueError:
                    print("❌ Invalid input.")
            
            elif choice == '2':
                # View Categories
                display_categories()
            
            elif choice == '3':
                # View Leaderboard
                game.display_leaderboard()
            
            elif choice == '4':
                # View Rules
                display_rules()
            
            else:
                print("❌ Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled.")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()