# Problem: 37. Sudoku Solver
# Difficulty: Hard
# Link: https://leetcode.com/problems/sudoku-solver/description

# Time Complexity: O(9^(Empty Cells)) - In the worst case, we might have 9 choices for every empty cell. However, Sudoku rules severely prune the decision tree, making it run extremely fast in practice.
# Space Complexity: O(1) - The board size is always 9x9, so the call stack and Hash Sets take constant space.

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize Fast Validation Sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Pre-fill sets with the given numbers and collect all empty cells
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
        # The Backtracking Engine
        def backtrack(index: int) -> bool:
            # Base Case: If we have successfully filled all empty cells, the board is solved!
            if index == len(empty_cells):
                return True
                
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing every digit from 1 to 9
            for digit in map(str, range(1, 10)):
                # Fast Validation Check
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    
                    # Choose
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)
                    
                    # Explore
                    if backtrack(index + 1):
                        return True
                        
                    # Unchoose (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
                    
            # If no digit 1-9 works, this path is a dead end. Trigger backtracking.
            return False
            
        # Start the recursive engine
        backtrack(0)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    sol.solveSudoku(board)
    
    print("Test 1: Solved Board")
    # Expected Output:
    # ['5', '3', '4', '6', '7', '8', '9', '1', '2']
    # ['6', '7', '2', '1', '9', '5', '3', '4', '8']
    # ['1', '9', '8', '3', '4', '2', '5', '6', '7']
    # ['8', '5', '9', '7', '6', '1', '4', '2', '3']
    # ['4', '2', '6', '8', '5', '3', '7', '9', '1']
    # ['7', '1', '3', '9', '2', '4', '8', '5', '6']
    # ['9', '6', '1', '5', '3', '7', '2', '8', '4']
    # ['2', '8', '7', '4', '1', '9', '6', '3', '5']
    # ['3', '4', '5', '2', '8', '6', '1', '7', '9']
    for row in board:
        print(row)