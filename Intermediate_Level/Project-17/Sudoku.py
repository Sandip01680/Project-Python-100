# 6x6 Sudoku Solver using Backtracking and Recursion

N = 6  # Sudoku grid size (6x6)

def print_grid(grid):
    """Prints the Sudoku grid neatly."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def is_safe(grid, row, col, num):
    """Check if num can be placed at grid[row][col]."""

    # Check row
    for x in range(N):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(N):
        if grid[x][col] == num:
            return False

    # Check 2x3 subgrid
    start_row = row - row % 2
    start_col = col - col % 3
    for i in range(2):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid, row=0, col=0):
    """Recursive Sudoku solver using Backtracking."""

    # ✅ Base case: If we reached the end, puzzle solved
    if row == N - 1 and col == N:
        return True

    # Move to next row if column exceeds limit
    if col == N:
        row += 1
        col = 0

    # Skip already filled cells
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1)

    # Try digits 1–6
    for num in range(1, N + 1):
        if is_safe(grid, row, col, num):
            grid[row][col] = num  # place number

            # 🔁 Recursion: solve next cell
            if solve_sudoku(grid, row, col + 1):
                return True

            # ❌ Backtracking: undo choice
            grid[row][col] = 0

    return False


# Example 6x6 Sudoku puzzle (0 = empty cell)
sudoku_grid_6x6 = [
    [0, 0, 3, 0, 6, 0],
    [0, 6, 0, 0, 0, 3],
    [3, 0, 0, 6, 0, 0],
    [0, 0, 6, 0, 0, 2],
    [5, 0, 0, 0, 2, 0],
    [0, 2, 0, 3, 0, 0]
]

print("Original 6x6 Sudoku Puzzle (Question):")
print_grid(sudoku_grid_6x6)

# Show motivational message
print("\n👉 Try it yourself... or I will give the answer!")

# Ask user if they want the answer
choice = input("\nDo you want me to solve it? (y/n): ")

if choice.lower() == "y":
    if solve_sudoku(sudoku_grid_6x6):
        print("\nSolved 6x6 Sudoku Puzzle (Answer):")
        print_grid(sudoku_grid_6x6)
    else:
        print("No solution exists.")
else:
    print("Okay, you can try solving it yourself!")