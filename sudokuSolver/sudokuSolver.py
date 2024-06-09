import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

    def create_grid(self):
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(
                    self.root,
                    bd=2,
                    relief='solid',
                    bg='black'  # Added for debugging, remove if not needed
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                self.create_subgrid(frame, i * 3, j * 3)

        solve_button = tk.Button(self.root, text="Validate", command=self.validate_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def create_subgrid(self, frame, start_row, start_col):
        for i in range(3):
            for j in range(3):
                cell = tk.Entry(frame, width=3, font=("Arial", 18), justify='center')
                cell.grid(row=i, column=j, padx=1, pady=1)
                self.cells[start_row + i][start_col + j] = cell

    def validate_puzzle(self):
        puzzle = []
        for row in self.cells:
            puzzle_row = []
            for cell in row:
                val = cell.get()
                if val == '':
                    puzzle_row.append(0)
                elif val.isdigit() and 1 <= int(val) <= 9:
                    puzzle_row.append(int(val))
                else:
                    messagebox.showerror("Invalid input", "Please enter numbers between 1 and 9")
                    return
            puzzle.append(puzzle_row)
        
        if self.is_valid_sudoku(puzzle):
            messagebox.showinfo("Valid", "The Sudoku puzzle is valid!")
        else:
            messagebox.showerror("Invalid", "The Sudoku puzzle is not valid.")

    def is_valid_sudoku(self, board):
        def is_valid_unit(unit):
            unit = [i for i in unit if i != 0]
            return len(unit) == len(set(unit))

        def is_valid_row(board):
            for row in board:
                if not is_valid_unit(row):
                    return False
            return True

        def is_valid_col(board):
            for col in zip(*board):
                if not is_valid_unit(col):
                    return False
            return True

        def is_valid_square(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                    if not is_valid_unit(square):
                        return False
            return True

        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
