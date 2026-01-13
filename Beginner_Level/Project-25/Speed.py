# Advanced Level

import time
import random
from datetime import datetime


# Test text samples organized by difficulty
TEXT_SAMPLES = {
    "easy": [
        "The quick brown fox jumps over the lazy dog near the river bank.",
        "A gentle breeze blows through the tall trees in the quiet park today.",
        "She sells seashells by the seashore during the warm summer months.",
        "The early bird catches the worm before the sun rises in the morning.",
        "Life is like riding a bicycle to keep your balance you must keep moving."
    ],
    "medium": [
        "Programming is the art of telling another human what one wants the computer to do.",
        "Success is not final failure is not fatal it is the courage to continue that counts.",
        "The only way to do great work is to love what you do and never settle for less.",
        "Technology is best when it brings people together and makes our lives easier.",
        "Practice makes perfect but nobody is perfect so why practice when you can innovate."
    ],
    "hard": [
        "Cryptography is the practice and study of techniques for secure communication in the presence of adversarial behavior.",
        "The phenomenon of quantum entanglement demonstrates that particles can be intrinsically connected regardless of distance.",
        "Artificial intelligence encompasses machine learning natural language processing and computer vision technologies.",
        "Philosophical discourse requires careful consideration of epistemological ontological and axiological perspectives.",
        "Neuroplasticity refers to the brain's ability to reorganize itself by forming new neural connections throughout life."
    ]
}


def get_random_text(difficulty="medium"):
    """Get random text sample based on difficulty."""
    return random.choice(TEXT_SAMPLES[difficulty])


def calculate_wpm(text, time_taken):
    """
    Calculate Words Per Minute (WPM).
    Standard: 1 word = 5 characters including spaces.
    
    Args:
        text (str): Text that was typed
        time_taken (float): Time in seconds
    
    Returns:
        float: Words per minute
    """
    if time_taken == 0:
        return 0
    
    # Calculate words (5 characters = 1 word)
    words = len(text) / 5
    minutes = time_taken / 60
    
    return words / minutes


def calculate_accuracy(original, typed):
    """
    Calculate typing accuracy as percentage.
    
    Args:
        original (str): Original text
        typed (str): User's typed text
    
    Returns:
        float: Accuracy percentage
    """
    if not typed:
        return 0.0
    
    # Compare character by character
    correct = 0
    total = max(len(original), len(typed))
    
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1
    
    return (correct / total) * 100


def count_errors(original, typed):
    """
    Count typing errors.
    
    Returns:
        dict: Dictionary with error statistics
    """
    errors = {
        "total": 0,
        "wrong_chars": 0,
        "missing_chars": 0,
        "extra_chars": 0
    }
    
    # Character comparison
    min_len = min(len(original), len(typed))
    
    for i in range(min_len):
        if original[i] != typed[i]:
            errors["wrong_chars"] += 1
            errors["total"] += 1
    
    # Missing or extra characters
    if len(typed) < len(original):
        errors["missing_chars"] = len(original) - len(typed)
        errors["total"] += errors["missing_chars"]
    elif len(typed) > len(original):
        errors["extra_chars"] = len(typed) - len(original)
        errors["total"] += errors["extra_chars"]
    
    return errors


def display_comparison(original, typed):
    """Display character-by-character comparison."""
    print("\n" + "=" * 80)
    print("CHARACTER COMPARISON")
    print("=" * 80)
    print("\nOriginal:")
    print(f"  {original}")
    print("\nYour typing:")
    print(f"  {typed}")
    print("\nDifferences:")
    
    # Show differences
    diff_line = "  "
    for i in range(max(len(original), len(typed))):
        if i >= len(typed):
            diff_line += "^"  # Missing character
        elif i >= len(original):
            diff_line += "+"  # Extra character
        elif original[i] != typed[i]:
            diff_line += "✗"  # Wrong character
        else:
            diff_line += " "  # Correct
    
    print(diff_line)
    print("\nLegend: ✗ = Wrong  ^ = Missing  + = Extra")
    print("=" * 80)


def display_results(original, typed, time_taken):
    """Display comprehensive test results."""
    wpm = calculate_wpm(typed, time_taken)
    accuracy = calculate_accuracy(original, typed)
    errors = count_errors(original, typed)
    
    # Gross WPM vs Net WPM
    gross_wpm = calculate_wpm(typed, time_taken)
    net_wpm = gross_wpm - (errors["total"] / (time_taken / 60))
    net_wpm = max(0, net_wpm)  # Don't go negative
    
    print("\n" + "=" * 80)
    print("TEST RESULTS")
    print("=" * 80)
    
    # Time and Speed
    print(f"\n⏱️  Time Taken:        {time_taken:.2f} seconds")
    print(f"⚡ Gross WPM:         {gross_wpm:.1f} words per minute")
    print(f"🎯 Net WPM:           {net_wpm:.1f} words per minute")
    
    # Accuracy
    print(f"\n📊 Accuracy:          {accuracy:.1f}%")
    
    # Character statistics
    print(f"\n📝 Characters Typed:  {len(typed)}")
    print(f"✓  Correct:           {len(typed) - errors['total']}")
    print(f"✗  Errors:            {errors['total']}")
    
    if errors["total"] > 0:
        print(f"   - Wrong chars:     {errors['wrong_chars']}")
        print(f"   - Missing chars:   {errors['missing_chars']}")
        print(f"   - Extra chars:     {errors['extra_chars']}")
    
    # Performance rating
    print(f"\n🏆 Performance:       {get_performance_rating(net_wpm, accuracy)}")
    
    print("=" * 80)


def get_performance_rating(wpm, accuracy):
    """Get performance rating based on WPM and accuracy."""
    if accuracy < 80:
        return "Focus on accuracy first!"
    elif wpm >= 80 and accuracy >= 95:
        return "🌟 EXPERT - Outstanding!"
    elif wpm >= 60 and accuracy >= 90:
        return "⭐ ADVANCED - Excellent work!"
    elif wpm >= 40 and accuracy >= 85:
        return "✨ INTERMEDIATE - Great progress!"
    elif wpm >= 25:
        return "🔰 BEGINNER - Keep practicing!"
    else:
        return "📚 NOVICE - Don't give up!"


def show_statistics_reference():
    """Display typing speed reference statistics."""
    print("\n" + "=" * 80)
    print("TYPING SPEED REFERENCE")
    print("=" * 80)
    
    print("\nAverage Typing Speeds (WPM):")
    print("  Novice:          < 25 WPM")
    print("  Beginner:        25-35 WPM")
    print("  Intermediate:    40-50 WPM")
    print("  Advanced:        60-70 WPM")
    print("  Expert:          80-100+ WPM")
    print("  Professional:    100-120+ WPM")
    
    print("\nWorld Records:")
    print("  Fastest typist:  216 WPM (Barbara Blackburn)")
    print("  Average pro:     65-75 WPM")
    
    print("\nAccuracy Guidelines:")
    print("  Excellent:       95-100%")
    print("  Good:            90-94%")
    print("  Acceptable:      85-89%")
    print("  Needs Practice:  < 85%")
    
    print("=" * 80)


def run_typing_test(difficulty="medium"):
    """Run a typing speed test."""
    # Get random text
    original_text = get_random_text(difficulty)
    
    print("\n" + "=" * 80)
    print("GET READY!")
    print("=" * 80)
    print(f"\nDifficulty: {difficulty.upper()}")
    print(f"Text length: {len(original_text)} characters")
    print("\nType the following text exactly as shown:")
    print("-" * 80)
    print(original_text)
    print("-" * 80)
    
    # Wait for user to be ready
    input("\nPress ENTER when ready to start...")
    
    print("\n🏁 START TYPING NOW! 🏁\n")
    
    # Start timer
    start_time = time.time()
    
    # Get user input
    typed_text = input()
    
    # Stop timer
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Display results
    display_results(original_text, typed_text, time_taken)
    
    # Show comparison if there are errors
    if typed_text != original_text:
        show_comparison = input("\nShow detailed comparison? (y/n): ")
        if show_comparison.lower() == 'y':
            display_comparison(original_text, typed_text)
    else:
        print("\n🎉 PERFECT! You typed it exactly right! 🎉")
    
    return {
        "wpm": calculate_wpm(typed_text, time_taken),
        "accuracy": calculate_accuracy(original_text, typed_text),
        "time": time_taken,
        "date": datetime.now()
    }


def save_results(results_list, filename="typing_results.txt"):
    """Save test results to file."""
    try:
        with open(filename, 'a') as f:
            for result in results_list:
                f.write(f"\n{'-' * 50}\n")
                f.write(f"Date: {result['date'].strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"WPM: {result['wpm']:.1f}\n")
                f.write(f"Accuracy: {result['accuracy']:.1f}%\n")
                f.write(f"Time: {result['time']:.2f}s\n")
        
        print(f"\n✓ Results saved to {filename}")
        return True
    except Exception as e:
        print(f"\n❌ Error saving results: {str(e)}")
        return False


def main():
    """Main program execution."""
    print("=" * 80)
    print("                    TYPING SPEED TEST")
    print("=" * 80)
    print("\nTest your typing speed and accuracy!")
    print("Results show WPM (Words Per Minute) and accuracy percentage.")
    
    test_results = []
    
    while True:
        print("\n" + "-" * 80)
        print("Options:")
        print("  1. Take typing test (Easy)")
        print("  2. Take typing test (Medium)")
        print("  3. Take typing test (Hard)")
        print("  4. View statistics reference")
        print("  5. Save results to file")
        print("  q. Quit")
        print("-" * 80)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            if test_results:
                save_opt = input("\nSave your results before quitting? (y/n): ")
                if save_opt.lower() == 'y':
                    save_results(test_results)
            
            print("\n👋 Keep practicing! Goodbye!")
            break
        
        try:
            if choice == '1':
                result = run_typing_test("easy")
                test_results.append(result)
            
            elif choice == '2':
                result = run_typing_test("medium")
                test_results.append(result)
            
            elif choice == '3':
                result = run_typing_test("hard")
                test_results.append(result)
            
            elif choice == '4':
                show_statistics_reference()
            
            elif choice == '5':
                if test_results:
                    save_results(test_results)
                else:
                    print("\n📋 No results to save yet. Take a test first!")
            
            else:
                print("\n❌ Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Test cancelled.")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()