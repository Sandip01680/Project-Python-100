# Beginner Level

import time
import random

def typing_speed_test():
    text_samples = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an amazing programming language.",
        "Artificial Intelligence is the future of technology.",
        "Data science is a blend of statistics and programming.",
        "Learning to code is a valuable skill in today's world."
    ]
    
    random_text = random.choice(text_samples)
    print("Type the following text as fast as you can:\n")
    print(random_text)
    input("\nPress Enter when you are ready to start...")
    
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_per_minute = (len(user_input.split()) / time_taken) * 60
    
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} words per minute")

typing_speed_test()
