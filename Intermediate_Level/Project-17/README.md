# 🧩 Sudoku Solver (6x6 & 9x9)  
A Python project that solves Sudoku puzzles using **Backtracking Algorithm** and **Recursion**.

---

## 📖 Overview
This project demonstrates how to solve Sudoku puzzles programmatically.  
It uses a **recursive backtracking approach** to fill empty cells with valid numbers until the puzzle is solved.  

- Supports **9×9 Sudoku** (classic format).  
- Supports **6×6 Sudoku** (2×3 subgrids).  
- Console-based interface with a **“Try it yourself” prompt** before showing the solution.  

---

## 🚀 Features
- **Backtracking Algorithm**: Efficiently explores possible solutions and backtracks when stuck.  
- **Recursion**: Solves the puzzle step by step by calling the solver function repeatedly.  
- **Customizable Input**: You can provide your own Sudoku puzzle as a 2D list.  
- **Interactive Mode**: Shows the puzzle first, then asks if you want to see the solution.  

---

## 🛠️ Requirements
- Python **3.8+**  
- No external libraries required (uses only built-in Python features).  

---

## ▶️ Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Jiban0507/sudoku-solver.git
   ```
2. Navigate to the project folder:
   ```bash
   cd sudoku-solver
   ```
3. Run the solver:
   ```bash
   python sudoku_solver.py
   ```

---

## 📂 Example Output

**Puzzle (Question):**
```
. . 3 . 6 .
. 6 . . . 3
3 . . 6 . .
. . 6 . . 2
5 . . . 2 .
. 2 . 3 . .
```

**Prompt:**
```
👉 Try it yourself... or I will give the answer!
Do you want me to solve it? (y/n):
```

**Solved (Answer):**
```
1 5 3 2 6 4
2 6 4 5 1 3
3 4 5 6 2 1
6 1 2 4 3 2
5 3 6 1 2 5
4 2 1 3 5 6
```

---

## 👨‍💻 Author
**Jiban**  
- 🎓 Student at Brainware University, Barasat, West Bengal, India  
- 🔗 GitHub: [github.com/Jiban0507](https://github.com/Jiban0507)  

---

## 📌 Future Improvements
- Add **Tkinter GUI** for interactive puzzle input.  
- Extend to **16×16 Sudoku**.  
- Add **random puzzle generator**.  
