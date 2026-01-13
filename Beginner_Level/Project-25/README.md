# Typing Speed Test ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)

Professional typing speed test application that measures WPM (Words Per Minute), accuracy, and provides detailed performance statistics.

## Features

### Comprehensive Testing
- **3 Difficulty Levels**: Easy, Medium, Hard
- **Random Text Samples**: 15 unique passages
- **Accurate Timing**: Precise millisecond measurement
- **Real-time Input**: Live typing capture

### Detailed Metrics
- **Gross WPM**: Raw typing speed
- **Net WPM**: Speed adjusted for errors
- **Accuracy Percentage**: Character-level precision
- **Error Analysis**: Wrong, missing, and extra characters
- **Performance Rating**: Skill level assessment

### Advanced Features
- **Character Comparison**: Visual diff of mistakes
- **Statistics Reference**: Industry standards and benchmarks
- **Result Saving**: Export results to file
- **Multiple Tests**: Track improvement over time
- **Performance Ratings**: Novice to Expert levels

## Requirements

- Python 3.x
- Built-in modules: `time`, `random`, `datetime`

## Installation

```bash
python typing_speed_test.py
```

## How to Use

### Main Menu
```
==================================================
                TYPING SPEED TEST
==================================================

Options:
  1. Take typing test (Easy)
  2. Take typing test (Medium)
  3. Take typing test (Hard)
  4. View statistics reference
  5. Save results to file
  q. Quit
```

### Taking a Test

#### Step 1: Select Difficulty
```
Your choice: 2

==================================================
GET READY!
==================================================

Difficulty: MEDIUM
Text length: 87 characters

Type the following text exactly as shown:
--------------------------------------------------------------------------------
Success is not final failure is not fatal it is the courage to continue that counts.
--------------------------------------------------------------------------------

Press ENTER when ready to start...
```

#### Step 2: Type the Text
```
🏁 START TYPING NOW! 🏁

[Type the text as quickly and accurately as possible]
```

#### Step 3: View Results
```
==================================================
TEST RESULTS
==================================================

⏱️  Time Taken:        45.32 seconds
⚡ Gross WPM:         55.3 words per minute
🎯 Net WPM:           51.8 words per minute

📊 Accuracy:          94.2%

📝 Characters Typed:  87
✓  Correct:           82
✗  Errors:            5
   - Wrong chars:     3
   - Missing chars:   2
   - Extra chars:     0

🏆 Performance:       ✨ INTERMEDIATE - Great progress!
==================================================
```

## Understanding the Metrics

### Words Per Minute (WPM)

#### Calculation Formula
```
1 word = 5 characters (standard)
WPM = (Characters typed / 5) / (Time in minutes)

Example:
- Typed: 250 characters
- Time: 60 seconds (1 minute)
- WPM = (250 / 5) / 1 = 50 WPM
```

#### Gross WPM vs Net WPM
- **Gross WPM**: Raw speed without error penalty
- **Net WPM**: `Gross WPM - (Errors / Time in minutes)`
- Net WPM is the true measure of typing skill

### Accuracy Percentage

```
Accuracy = (Correct characters / Total characters) × 100

Example:
- Original: 100 characters
- Correct: 95 characters
- Accuracy = (95 / 100) × 100 = 95%
```

### Error Types

| Error Type | Description | Example |
|------------|-------------|---------|
| Wrong char | Typed different character | Original: 'a', Typed: 's' |
| Missing char | Didn't type a character | Original: 'cat', Typed: 'ct' |
| Extra char | Typed additional character | Original: 'cat', Typed: 'cast' |

## Difficulty Levels

### Easy
- **Length**: 50-70 characters
- **Vocabulary**: Common, simple words
- **Punctuation**: Basic
- **Example**: "The quick brown fox jumps over the lazy dog."

### Medium
- **Length**: 75-95 characters
- **Vocabulary**: Standard English
- **Punctuation**: Moderate
- **Example**: "Success is not final failure is not fatal it is the courage to continue."

### Hard
- **Length**: 100-130 characters
- **Vocabulary**: Advanced, technical
- **Punctuation**: Complex
- **Example**: "Cryptography is the practice and study of techniques for secure communication."

## Typing Speed Reference

### Average Speeds

| Level | WPM Range | Description |
|-------|-----------|-------------|
| Novice | < 25 | Just starting |
| Beginner | 25-35 | Basic proficiency |
| Intermediate | 40-50 | Comfortable typing |
| Advanced | 60-70 | Skilled typist |
| Expert | 80-100+ | Professional level |
| Professional | 100-120+ | Elite typist |

### Accuracy Standards

| Rating | Accuracy | Assessment |
|--------|----------|------------|
| Excellent | 95-100% | Perfect precision |
| Good | 90-94% | Minor mistakes |
| Acceptable | 85-89% | Room for improvement |
| Poor | < 85% | Needs practice |

### World Records
- **Fastest**: 216 WPM (Barbara Blackburn, 2005)
- **Average Professional**: 65-75 WPM
- **Average Person**: 40-45 WPM
- **Hunt and Peck**: 10-30 WPM

## Performance Ratings

### 🌟 EXPERT
- **Requirements**: 80+ WPM, 95%+ accuracy
- **Status**: Outstanding professional level
- **Career**: Ready for data entry, transcription

### ⭐ ADVANCED
- **Requirements**: 60+ WPM, 90%+ accuracy
- **Status**: Excellent typing skills
- **Career**: Most office jobs

### ✨ INTERMEDIATE
- **Requirements**: 40+ WPM, 85%+ accuracy
- **Status**: Competent typist
- **Career**: Standard office work

### 🔰 BEGINNER
- **Requirements**: 25+ WPM
- **Status**: Basic proficiency
- **Goal**: Keep practicing!

### 📚 NOVICE
- **Requirements**: < 25 WPM
- **Status**: Learning phase
- **Goal**: Focus on technique

## Character Comparison Feature

Shows exactly where mistakes occurred:

```
Character Comparison
==================================================

Original:
  The quick brown fox jumps over the lazy dog.

Your typing:
  The qiuck brown fox jumsp over teh lazy dog.

Differences:
     ✗          ✗       ✗✗

Legend: ✗ = Wrong  ^ = Missing  + = Extra
==================================================
```

## Result Saving

Results are saved to `typing_results.txt`:

```
--------------------------------------------------
Date: 2024-12-28 14:30:45
WPM: 51.8
Accuracy: 94.2%
Time: 45.32s
--------------------------------------------------
Date: 2024-12-28 14:35:22
WPM: 58.3
Accuracy: 96.1%
Time: 38.15s
--------------------------------------------------
```

## Use Cases

### Personal Development
- Track typing improvement over time
- Practice for job requirements
- Prepare for typing tests
- Build muscle memory

### Professional
- Data entry jobs (require 50-80 WPM)
- Transcription work (require 60-100 WPM)
- Administrative positions
- Programming (faster coding)

### Educational
- Typing class assessments
- Computer literacy courses
- Skill certification
- Student progress tracking

### Competitive
- Typing competitions
- Speed challenges
- Personal records
- Group competitions

## Tips to Improve Typing Speed

### Technique
1. **Touch Typing**: Learn to type without looking
2. **Home Row**: Keep fingers on ASDF JKL;
3. **Posture**: Sit upright, feet flat
4. **Hand Position**: Wrists straight, not bent

### Practice
1. **Daily Practice**: 15-30 minutes per day
2. **Accuracy First**: Speed comes with accuracy
3. **Common Words**: Practice frequent words
4. **Difficult Keys**: Focus on problem keys

### Resources
- **Typing.com**: Free lessons
- **Keybr.com**: Algorithm-based practice
- **10FastFingers**: Speed tests
- **TypeRacer**: Competitive typing

## Common Mistakes to Avoid

### Speed Over Accuracy
- ❌ Rushing causes more errors
- ✅ Build speed gradually with accuracy

### Looking at Keyboard
- ❌ Slows you down long-term
- ✅ Practice touch typing blind

### Poor Posture
- ❌ Causes fatigue and errors
- ✅ Maintain ergonomic position

### Irregular Practice
- ❌ Sporadic practice yields poor results
- ✅ Consistent daily practice

## Keyboard Layout Mastery

### QWERTY Home Row
```
Left Hand:  A S D F
Right Hand: J K L ;
```

### Finger Assignments
- **Pinkies**: Q A Z / P ; /
- **Ring**: W S X / O L .
- **Middle**: E D C / I K ,
- **Index**: R F V B / U J N M

## Code Structure

```python
# Text samples database
TEXT_SAMPLES = {
    "easy": [...],
    "medium": [...],
    "hard": [...]
}

# Core functions
get_random_text(difficulty)           # Select random text
calculate_wpm(text, time)             # Calculate WPM
calculate_accuracy(original, typed)   # Calculate accuracy %
count_errors(original, typed)         # Detailed error count
display_comparison(original, typed)   # Show character diff
display_results(...)                  # Format and display results
get_performance_rating(wpm, accuracy) # Assess skill level
run_typing_test(difficulty)           # Main test execution
save_results(results_list, filename)  # Export to file
```

## Customization

### Adding Text Samples
```python
TEXT_SAMPLES["easy"].append(
    "Your new easy text sample here."
)
```

### Adjusting Performance Ratings
```python
# Modify thresholds in get_performance_rating()
if wpm >= 100 and accuracy >= 98:
    return "MASTER - Professional level!"
```

### Custom Scoring
```python
# Add bonus points for perfect accuracy
if accuracy == 100:
    wpm *= 1.1  # 10% bonus
```

## Advanced Features

### Progress Tracking
Track improvement over multiple sessions:
- Average WPM trend
- Accuracy improvement
- Personal best records
- Practice consistency

### Goal Setting
Set targets:
- Reach 60 WPM
- Maintain 95% accuracy
- Complete 10 tests per week
- Beat personal best

## Troubleshooting

### Input Not Capturing
- Press Enter only once
- Don't paste text
- Check keyboard connection

### Timer Issues
- Don't pause during test
- Complete in one session
- Restart if interrupted

### Accuracy Too Low
- Slow down initially
- Focus on correct keys
- Practice problem characters
- Check hand position

## Best Practices

1. **Warm Up**: Start with easy tests
2. **Regular Breaks**: Every 15-20 minutes
3. **Track Progress**: Save all results
4. **Stay Relaxed**: Tension slows you down
5. **Be Patient**: Improvement takes time

## License

Free to use and modify for educational and personal purposes.

## Author Notes

Professional typing test application following industry standards for WPM calculation and accuracy measurement. Designed to help users improve their typing skills with comprehensive feedback and performance tracking.