import time
import random
import sys

# Sentences by difficulty level
sentences = {
    "easy": [
        "Python is fun.",
        "Typing is easy.",
        "Practice daily."
    ],
    "medium": [
        "Python is a powerful programming language used for web development and data science.",
        "Typing speed tests help improve accuracy and efficiency in everyday computer use.",
        "Practice makes perfect when learning coding and typing together."
    ],
    "hard": [
        "Libraries and functions in Python allow developers to build complex applications with efficiency and clarity.",
        "Typing speed and accuracy are essential skills for programmers, writers, and students in the digital age.",
        "Consistent practice with challenging paragraphs improves both cognitive focus and muscle memory in typing."
    ]
}

# Function to calculate typing speed and mistakes
def calculate_speed(start_time, end_time, typed_text, reference_text):
    elapsed_time = end_time - start_time
    words = typed_text.split()
    num_words = len(words)
    
    # Words per minute (WPM)
    wpm = (num_words / elapsed_time) * 60
    
    # Accuracy + Wrong words calculation
    typed_words = typed_text.split()
    reference_words = reference_text.split()
    correct = 0
    wrong_words = []
    
    for tw, rw in zip(typed_words, reference_words):
        if tw == rw:
            correct += 1
        else:
            wrong_words.append((rw, tw))  # (expected, typed)
    
    accuracy = (correct / len(reference_words)) * 100
    
    return wpm, accuracy, elapsed_time, wrong_words

# Function to format time
def format_time(seconds):
    minutes, sec = divmod(int(seconds), 60)
    return f"{minutes} minute {sec} second"

# Highlight text (yellow + bold)
def highlight_text(text):
    return f"\033[1;33m{text}\033[0m"

# Color-coded word comparison
def color_words(reference_text, typed_text):
    ref_words = reference_text.split()
    typed_words = typed_text.split()
    colored_output = []
    
    for rw, tw in zip(ref_words, typed_words):
        if rw == tw:
            colored_output.append(f"\033[1;32m{tw}\033[0m")  # Green for correct
        else:
            colored_output.append(f"\033[1;31m{tw}\033[0m")  # Red for wrong
    
    return " ".join(colored_output)

# Typing test function
def typing_test():
    print("Choose difficulty level: easy / medium / hard")
    level = input("Enter level: ").lower()
    if level not in sentences:
        print("Invalid choice! Defaulting to medium.")
        level = "medium"
    
    reference_text = random.choice(sentences[level])
    print("\nType the following paragraph as fast and accurately as you can:\n")
    print(highlight_text(reference_text))  # Highlighted paragraph
    
    input("\nPress Enter when you are ready to start...")
    
    # Countdown
    for i in range(3, 0, -1):
        sys.stdout.write(f"\rStarting in {i}...")
        sys.stdout.flush()
        time.sleep(1)
    print("\nGo!\n")
    
    start_time = time.time()
    typed_text = input("Start typing here:\n")
    end_time = time.time()
    
    wpm, accuracy, elapsed_time, wrong_words = calculate_speed(start_time, end_time, typed_text, reference_text)
    
    print("\n--- Results ---")
    print(f"Time taken: {format_time(elapsed_time)}")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    
    # Show color-coded typed sentence
    print("\nYour typing with highlights:")
    print(color_words(reference_text, typed_text))
    
    if wrong_words:
        print("\nWrongly typed words:")
        for expected, typed in wrong_words:
            print(f"Expected: '{expected}' | You typed: '{typed}'")
    else:
        print("\nNo mistakes! Well done 🎉")

if __name__ == "__main__":
    typing_test()