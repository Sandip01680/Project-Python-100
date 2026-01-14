# 🎓 Interactive Quiz Application

A simple, interactive command-line quiz application built with Python that tests your knowledge on various topics including geography, programming, science, and general knowledge.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)
![Code Style](https://img.shields.io/badge/code%20style-PEP8-blue.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Quick Start](#-quick-start)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Customization Guide](#-customization-guide)
- [Project Structure](#-project-structure)
- [Features vs Enhancements](#-features-vs-enhancements)
- [Code Improvements](#-code-improvements)
- [Future Enhancements](#-future-enhancements)
- [Community Guidelines](#-community-guidelines)
- [Contributing](#-contributing)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)

## ✨ Features

- **Interactive Quiz Interface**: User-friendly command-line interface with clear question formatting
- **Multiple Choice Questions**: 10 diverse questions covering various topics
- **Input Validation**: Robust validation to ensure only valid answers (A, B, C, D) are accepted
- **Real-time Feedback**: Immediate feedback on correct/incorrect answers
- **Score Calculation**: Automatic score calculation with percentage display
- **Pass/Fail System**: Results displayed based on a 50% pass threshold
- **Error Handling**: Graceful handling of user interruptions and errors
- **Clean Code Structure**: Well-organized, maintainable code with proper documentation

## 🎬 Demo

### Screenshots

#### Quiz Start - Questions 1-2

![Quiz Application - Start](screenshots/demo-screenshot-1.png)

*The quiz begins with a welcome message and displays questions with multiple-choice options. Users receive immediate feedback (✅ Correct!) after each answer.*

#### Quiz Completion - Final Results

![Quiz Application - Results](screenshots/demo-screenshot-2.png)

*After completing all 10 questions, the quiz displays the final score, percentage, and pass/fail result. In this example, the user scored 9/10 (90%) and passed the quiz.*

## ⚡ Quick Start

Get up and running in 3 simple steps:

```bash
# 1. Clone or download the repository
git clone <repository-url>
cd Project-26

# 2. Verify Python is installed
python --version  # Should be 3.6 or higher

# 3. Run the quiz
python Quiz.py
```

That's it! Start answering questions and test your knowledge! 🚀

## 🔧 Requirements

- **Python 3.6+** (Tested on Python 3.6 and above)
- No external dependencies required (uses only Python standard library)

## 📦 Installation

1. **Clone or download** this repository to your local machine

2. **Navigate** to the project directory:
   ```bash
   cd Project-26
   ```

3. **Verify Python installation**:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

## 🚀 Usage

1. **Run the quiz application**:
   ```bash
   python Quiz.py
   ```
   or
   ```bash
   python3 Quiz.py
   ```

2. **Follow the prompts**:
   - Read each question carefully
   - Enter your answer (A, B, C, or D)
   - Receive immediate feedback
   - View your final score and result at the end

### Example Output

```
************************************************************
🎓 Welcome to the Interactive Quiz!
************************************************************

Question 1: What is the capital of India?

A. Delhi
B. Mumbai
C. Kolkata
D. Chennai
Enter your answer (A/B/C/D): A
✅ Correct!

...

============================================================
🎯 Quiz Completed!
============================================================
Your final score: 8/10 (80.00%)
🏆 Result: PASS
============================================================
```

## 🛠️ Customization Guide

### Adding New Questions

To add new questions, simply add a new dictionary to the `quiz` list in `Quiz.py`:

```python
{
    "question": "Your question here?",
    "options": ["A. Option 1", "B. Option 2", "C. Option 3", "D. Option 4"],
    "answer": "A"  # The correct answer (A, B, C, or D)
}
```

**Example:**
```python
{"question": "What is 2 + 2?",
 "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
 "answer": "B"}
```

### Changing Pass Threshold

Modify the `PASS_THRESHOLD` constant at the top of `Quiz.py`:

```python
PASS_THRESHOLD = 70  # Change from 50 to 70 (or any value 0-100)
```

### Customizing Welcome Message

Edit the welcome message in the `run_quiz()` function:

```python
print("*" * 60)
print("🎓 Your Custom Welcome Message Here!")
print("*" * 60)
```

### Changing Answer Options

To support more answer options (e.g., A-E), modify the `VALID_ANSWERS` constant:

```python
VALID_ANSWERS = ["A", "B", "C", "D", "E"]
```

**Note:** Remember to update your question dictionaries to include option E.

### Customizing Output Formatting

You can modify the separator characters in the `run_quiz()` function:

```python
print("=" * 60)  # Change "=" to "-", "*", "#", etc.
```

## 📁 Project Structure

```
Project-26/
│
├── Quiz.py                # Main quiz application file
├── README.md              # Project documentation
├── screenshots/           # Screenshots directory
│   ├── README.md          # Screenshots guide
│   ├── demo-screenshot-1.png  # Screenshot 1: Quiz start
│   └── demo-screenshot-2.png  # Screenshot 2: Quiz results
└── demo.gif              # Demo GIF (optional, root directory)
```

## 📊 Features vs Enhancements

| Feature | Current Status | Future Enhancement |
|---------|---------------|-------------------|
| **Question Types** | ✅ Multiple Choice (A-D) | 🔄 True/False, Fill-in-the-blank |
| **Question Count** | ✅ 10 Questions | 🔄 Configurable question count |
| **Categories** | ❌ Not Available | 🔄 Topic-based categories |
| **Difficulty Levels** | ❌ Not Available | 🔄 Easy, Medium, Hard levels |
| **Timer** | ❌ Not Available | 🔄 Time limit per question |
| **Score Tracking** | ✅ Current session only | 🔄 Score history & statistics |
| **Question Bank** | ✅ Hardcoded in code | 🔄 JSON/CSV file support |
| **Randomization** | ❌ Sequential order | 🔄 Random question selection |
| **User Interface** | ✅ Command-line | 🔄 GUI (tkinter/PyQt) |
| **Results Export** | ❌ Not Available | 🔄 Export to CSV/JSON/TXT |
| **Multi-language** | ❌ English only | 🔄 Multi-language support |
| **Hints** | ❌ Not Available | 🔄 Hint system for questions |
| **Review Mode** | ❌ Not Available | 🔄 Review incorrect answers |

**Legend:**
- ✅ = Currently Available
- ❌ = Not Available
- 🔄 = Planned for Future

## 🔄 Code Improvements

The following improvements were made to enhance code quality and maintainability:

1. **Added Module Documentation**: Comprehensive docstrings for better code understanding
2. **Constants Extraction**: Moved magic numbers (pass threshold, valid answers) to constants for easier maintenance
3. **Error Handling**: Added try-except blocks for graceful error handling and user interruption support
4. **Input Validation Enhancement**: Improved input validation with `.strip()` for whitespace handling
5. **Main Guard**: Added `if __name__ == "__main__"` for proper script execution
6. **Function Documentation**: Added docstrings to all functions explaining parameters and return values
7. **Better Formatting**: Enhanced output formatting with separators for better readability
8. **Code Organization**: Improved code structure and readability
9. **Type Safety**: Better handling of edge cases and user interruptions

## 🎯 Future Enhancements

Potential improvements for future versions:

- [ ] **Question Categories**: Organize questions by topics (Geography, Programming, Science, etc.)
- [ ] **Difficulty Levels**: Add easy, medium, and hard difficulty levels
- [ ] **Timer Feature**: Add time limit for each question
- [ ] **Score History**: Save and display previous quiz scores
- [ ] **Question Bank Expansion**: Add more questions with a database or JSON file
- [ ] **Random Question Selection**: Randomly select questions from a larger pool
- [ ] **Multiple Quiz Modes**: Support for different quiz types (timed, practice, exam mode)
- [ ] **GUI Version**: Create a graphical user interface using tkinter or PyQt
- [ ] **Export Results**: Save quiz results to a file (CSV, JSON, or text)
- [ ] **Statistics Dashboard**: Show detailed statistics (time per question, category performance)

## 👥 Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please follow these guidelines:

- **Be Respectful**: Treat all community members with respect and kindness
- **Be Constructive**: Provide helpful feedback and suggestions
- **Be Open**: Welcome new ideas and different perspectives
- **Be Professional**: Maintain a professional tone in all interactions

### Reporting Issues

When reporting issues, please include:
- **Description**: Clear description of the issue
- **Steps to Reproduce**: Detailed steps to reproduce the problem
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: Python version, OS, etc.

### Feature Requests

When requesting features:
- **Use Case**: Explain why this feature would be useful
- **Proposed Solution**: Describe how you envision the feature working
- **Alternatives**: Mention any alternative solutions you've considered

### Pull Request Guidelines

- **Code Quality**: Ensure your code follows PEP 8 style guidelines
- **Documentation**: Update README.md if you add new features
- **Testing**: Test your changes thoroughly before submitting
- **Description**: Provide a clear description of your changes
- **Small Commits**: Keep commits focused and atomic

### Communication Channels

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and general discussion
- **Pull Requests**: Use Pull Requests for code contributions

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes** following the code style and guidelines
4. **Test your changes** thoroughly
5. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
6. **Push to the branch** (`git push origin feature/AmazingFeature`)
7. **Open a Pull Request** with a clear description

### Contribution Types

We welcome various types of contributions:

- 🐛 **Bug Fixes**: Fix existing issues
- ✨ **New Features**: Add new functionality
- 📝 **Documentation**: Improve documentation
- 🎨 **UI/UX**: Enhance user experience
- ⚡ **Performance**: Optimize code performance
- 🧪 **Tests**: Add or improve tests
- 🌐 **Translations**: Add multi-language support

## 🙏 Acknowledgements

We would like to thank the following:

- **Python Community**: For the amazing Python programming language and its extensive standard library
- **Project-Python-100**: For providing the inspiration and structure for this beginner-level project
- **Open Source Contributors**: All contributors who help improve this project
- **Educational Resources**: Various online resources that helped in learning Python fundamentals

### Resources Used

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Real Python](https://realpython.com/) - For Python best practices
- [GitHub Community Guidelines](https://docs.github.com/en/communities) - For community standards

### Inspiration

This project is part of the **Python 100 Projects** series, designed to help beginners learn Python through hands-on projects. The goal is to build practical applications while learning fundamental programming concepts.

**Special Thanks** to all the learners and educators who use and improve this project! 🎉

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Project-Python-100 - Beginner Level**

Part of the Python 100 Projects series focusing on beginner-level applications.

---

**Note**: This is a beginner-level project designed for learning Python fundamentals including:
- Data structures (lists, dictionaries)
- Functions and modular programming
- Input/output handling
- Control flow (loops, conditionals)
- Error handling
- Code organization and best practices

---

⭐ If you find this project helpful, please consider giving it a star!
