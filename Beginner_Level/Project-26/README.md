# Simple Quiz Game ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)

Professional multiple-choice quiz game with categories, scoring system, streaks, time bonuses, and leaderboard tracking.

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)
![Code Style](https://img.shields.io/badge/code%20style-PEP8-blue.svg)


## Features

### Quiz Categories
- **General Knowledge**: Geography, history, arts (5 questions)
- **Science**: Chemistry, biology, physics (5 questions)
- **Technology**: Computers, internet, inventions (5 questions)
- **Sports**: Olympics, soccer, basketball (5 questions)
- **Mixed Mode**: Questions from all categories

### Scoring System
- **Base Points**: 10 (easy), 20 (medium), 30 (hard)
- **Time Bonus**: Up to +10 points for quick answers
- **Streak Bonus**: +5 points per consecutive correct answer
- **Max Streak Bonus**: +25 points

### Game Features
- **Multiple Difficulty Levels**: Easy, Medium, Hard
- **Streak Tracking**: Consecutive correct answers
- **Time Tracking**: Answer speed measurement
- **Instant Feedback**: Immediate result display
- **Leaderboard**: Top 10 high scores
- **Performance Ratings**: 5 achievement levels

## Requirements

- Python 3.x
- Built-in modules: `json`, `os`, `random`, `datetime`

## Installation

```bash
python quiz_game.py
```

## Quick Start

### First Game
```
==================================================
            🎮 SIMPLE QUIZ GAME 🎮
==================================================

Main Menu:
  1. Play Quiz

Your choice: 1

📚 QUIZ CATEGORIES
--------------------------------------------------
  1. General Knowledge (5 questions)
  2. Science (5 questions)
  3. Technology (5 questions)
  4. Sports (5 questions)
  5. Mixed (All categories)

Select category: 1
How many questions? (5-10, default 5): 5
```

### Playing a Question
```
==================================================
🎮 QUIZ: General Knowledge
==================================================
Questions: 5
Instructions: Select the correct answer (1-4)

----------------------------------------------------------------------
Question 1/5
Difficulty: EASY
----------------------------------------------------------------------

What is the capital of France?

  1. London
  2. Berlin
  3. Paris
  4. Madrid

Your answer (1-4): 3

✅ CORRECT! +20 points
   Time: 3.2s
   Score: 20
```

### Results Screen
```
==================================================
📊 QUIZ RESULTS
==================================================

🎯 Performance:
   Total Questions:   5
   Correct Answers:   4
   Wrong Answers:     1
   Accuracy:          80.0%

💯 Scoring:
   Final Score:       95
   Best Streak:       3

🏆 Rating: ⭐ GREAT! Well done!
==================================================

Enter your name for the leaderboard: Alex

🎉 Congratulations! You ranked #3 on the leaderboard!
```

## Main Menu Options

### 1. Play Quiz
Start a new quiz game.

**Steps:**
1. Select category (1-5)
2. Choose number of questions (5-10)
3. Answer multiple-choice questions
4. View results and save score

### 2. View Categories
Browse available quiz categories and question counts.

```
==================================================
📚 QUIZ CATEGORIES
==================================================
  1. General Knowledge (5 questions)
  2. Science (5 questions)
  3. Technology (5 questions)
  4. Sports (5 questions)
  5. Mixed (All categories)
==================================================
```

### 3. View Leaderboard
See top 10 high scores.

```
==================================================
🏆 LEADERBOARD - TOP 10 SCORES
==================================================
Rank   Name            Score      Category              Questions    Accuracy   Date
------------------------------------------------------------------------------------------
🥇     Alex            150        General Knowledge     10           90.0%      2024-12-28
🥈     Sarah           145        Science               10           85.0%      2024-12-27
🥉     Mike            135        Technology            8            87.5%      2024-12-28
==================================================
```

### 4. View Rules & Scoring
Complete guide to game mechanics.

```
==================================================
📖 GAME RULES & SCORING
==================================================

🎯 How to Play:
  1. Select a quiz category
  2. Choose number of questions (5-10)
  3. Answer multiple-choice questions
  4. Get instant feedback on each answer
  5. View final score and accuracy

💯 Scoring System:
  • Easy questions:    10 points
  • Medium questions:  20 points
  • Hard questions:    30 points

⚡ Bonus Points:
  • Time bonus:        +10 points (under 5 seconds)
  • Time bonus:        +5 points (5-10 seconds)
  • Streak bonus:      +5 points per correct in a row
  • Max streak bonus:  +25 points
==================================================
```

## Scoring System Explained

### Base Points by Difficulty

| Difficulty | Points | Example |
|------------|--------|---------|
| Easy | 10 | "What is H2O?" |
| Medium | 20 | "What is the chemical symbol for gold?" |
| Hard | 30 | "How many bones in adult human body?" |

### Time Bonus

Answer quickly for extra points:

| Time Taken | Bonus Points |
|------------|--------------|
| < 5 seconds | +10 |
| 5-10 seconds | +5 |
| > 10 seconds | 0 |

### Streak Bonus

Consecutive correct answers multiply your score:

| Streak Length | Bonus Points |
|---------------|--------------|
| 1 correct | 0 |
| 2 in a row | +5 |
| 3 in a row | +10 |
| 4 in a row | +15 |
| 5+ in a row | +25 (max) |

### Score Calculation Example

**Question:** "What is the capital of France?" (Easy, 10 points)
- **Answer time:** 4 seconds
- **Current streak:** 2 correct in a row

**Calculation:**
```
Base points:      10
Time bonus:       +10 (under 5 seconds)
Streak bonus:     +10 (2 in a row × 5)
─────────────────────
Total:            30 points
```

## Performance Ratings

Your final accuracy determines your rating:

| Accuracy | Rating | Emoji | Description |
|----------|--------|-------|-------------|
| 90-100% | Excellent | 🌟 | Outstanding performance! |
| 75-89% | Great | ⭐ | Well done! |
| 60-74% | Good | ✨ | Keep practicing! |
| 40-59% | Fair | 🔰 | Room for improvement! |
| 0-39% | Needs Work | 📚 | Study more! |

## Quiz Categories Details

### General Knowledge
- Geography (capitals, oceans)
- History (world events, dates)
- Arts (famous artists, works)
- **Difficulty Mix**: Mostly easy/medium

### Science
- Chemistry (symbols, compounds)
- Biology (anatomy, organisms)
- Physics (speed of light, forces)
- **Difficulty Mix**: Medium/hard focus

### Technology
- Computing (CPU, HTML)
- Internet (WWW inventor)
- Innovations (iPhone release)
- **Difficulty Mix**: Easy/medium

### Sports
- Olympics (rings, events)
- Soccer (World Cup, rules)
- Basketball (hoop size, gameplay)
- **Difficulty Mix**: Easy/medium/hard

### Mixed Mode
- Random questions from all categories
- Balanced difficulty distribution
- Maximum variety

## Leaderboard System

### What Gets Saved
- **Name**: Player identifier
- **Score**: Total points earned
- **Category**: Quiz category played
- **Questions**: Number of questions answered
- **Accuracy**: Percentage correct
- **Date**: Timestamp of achievement

### Ranking Logic
1. Sorted by **score** (highest first)
2. Keeps **top 10** entries only
3. Older entries dropped if score too low
4. Ties broken by date (earlier = higher rank)

### File Format
Stored in `quiz_leaderboard.json`:

```json
[
  {
    "name": "Alex",
    "score": 150,
    "category": "General Knowledge",
    "questions": 10,
    "accuracy": 90.0,
    "date": "2024-12-28 14:30:45"
  }
]
```

## Strategy & Tips

### Maximize Your Score

#### 1. Answer Quickly
- Read question carefully but don't overthink
- Time bonus only for <10 second answers
- +10 points for <5 seconds is significant

#### 2. Build Streaks
- Streak bonus compounds rapidly
- 5-answer streak = +25 points bonus
- Focus on accuracy to maintain streaks

#### 3. Choose Harder Questions
- Hard questions worth 3× easy questions
- Risk vs. reward: accuracy matters
- Mixed mode balances both

#### 4. Practice Categories
- Review questions before playing
- Learn from wrong answers
- Replay weak categories

### Study Recommendations

**Before Playing:**
- Read through all questions
- Note difficult questions
- Research unfamiliar topics

**During Game:**
- Stay calm and focused
- Don't rush if unsure
- Trust your first instinct

**After Playing:**
- Review missed questions
- Study correct answers
- Track improvement over time

## Question Database Structure

### Question Format
```python
{
    "question": "What is the capital of France?",
    "options": ["London", "Berlin", "Paris", "Madrid"],
    "answer": 2,  # Index of correct option (0-based)
    "difficulty": "easy"  # "easy", "medium", or "hard"
}
```

### Adding Custom Questions

Edit the `QUIZ_DATABASE` dictionary:

```python
QUIZ_DATABASE = {
    "Your Category": [
        {
            "question": "Your question here?",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": 0,  # Correct answer index
            "difficulty": "medium"
        }
    ]
}
```

## Code Structure

### Classes

```python
class QuizGame:
    # Properties
    leaderboard_file, leaderboard
    current_score, total_questions
    correct_answers, wrong_answers
    current_streak, best_streak
    
    # Methods
    load_leaderboard()          # Load from JSON
    save_leaderboard()          # Save to JSON
    add_to_leaderboard(...)     # Add new score
    display_leaderboard()       # Show top 10
    calculate_score(...)        # Compute points
    reset_game()                # Clear stats
    play_quiz(category, num, shuffle)  # Main game loop
    display_results(category)   # Show final stats
```

### Main Functions

```python
display_categories()            # Show available categories
display_rules()                 # Show game rules
main()                          # Program entry point
```

## Use Cases

### Educational
- **Classroom quizzes**: Test student knowledge
- **Study tool**: Prepare for exams
- **Homework**: Interactive assignments
- **Trivia nights**: Group activities

### Entertainment
- **Family game night**: Competitive fun
- **Party games**: Social activity
- **Brain training**: Mental exercise
- **Time killer**: Quick entertainment

### Professional
- **Training**: Employee onboarding
- **Certification**: Practice tests
- **Team building**: Office activities
- **Assessments**: Knowledge evaluation

## Customization Ideas

### Easy Modifications

#### 1. Add More Questions
```python
QUIZ_DATABASE["Science"].append({
    "question": "What is DNA?",
    "options": ["Acid", "Base", "Genetic material", "Protein"],
    "answer": 2,
    "difficulty": "medium"
})
```

#### 2. Adjust Scoring
```python
base_scores = {
    "easy": 15,     # Changed from 10
    "medium": 25,   # Changed from 20
    "hard": 40      # Changed from 30
}
```

#### 3. Add Categories
```python
QUIZ_DATABASE["History"] = [
    {
        "question": "When did WWI begin?",
        "options": ["1912", "1914", "1916", "1918"],
        "answer": 1,
        "difficulty": "medium"
    }
]
```

### Advanced Features

#### True/False Questions
```python
# Add boolean question type
{
    "question": "Is Python a compiled language?",
    "options": ["True", "False"],
    "answer": 1,
    "difficulty": "medium"
}
```

#### Timed Mode
```python
# Add time limit per question
max_time_per_question = 30  # seconds
```

#### Difficulty Selection
```python
# Filter questions by difficulty
def get_questions_by_difficulty(difficulty):
    return [q for q in questions if q["difficulty"] == difficulty]
```

## Performance Benchmarks

### Typical Scores

| Skill Level | Score Range | Accuracy |
|-------------|-------------|----------|
| Beginner | 0-50 | < 50% |
| Intermediate | 50-100 | 50-75% |
| Advanced | 100-150 | 75-90% |
| Expert | 150+ | 90%+ |

### Time Estimates
- **5 questions**: 3-5 minutes
- **10 questions**: 6-10 minutes
- **Mixed category**: 5-8 minutes

## Troubleshooting

### Leaderboard Not Saving
- Check file permissions
- Ensure disk space available
- Verify JSON format valid

### Questions Repeating
- Not enough questions in category
- Increase question pool size
- Use mixed mode for variety

### Score Seems Wrong
- Check time bonus calculation
- Verify streak counter
- Review difficulty multipliers

## Future Enhancements

- [ ] Multiplayer mode
- [ ] Question timer display
- [ ] Hint system (costs points)
- [ ] Achievements/badges
- [ ] Question difficulty voting
- [ ] User-submitted questions
- [ ] Category difficulty ratings
- [ ] Export results to PDF
- [ ] Audio questions
- [ ] Image-based questions

## Educational Benefits

### Cognitive Skills
- **Knowledge retention**: Spaced repetition
- **Quick thinking**: Time pressure
- **Decision making**: Multiple choices
- **Pattern recognition**: Question types

### Learning Outcomes
- Broad knowledge base
- Subject mastery
- Test-taking skills
- Competitive motivation

## License

Free to use and modify for educational and entertainment purposes.

## Credits

Built with educational gaming principles to make learning fun and engaging through gamification, immediate feedback, and competitive elements.