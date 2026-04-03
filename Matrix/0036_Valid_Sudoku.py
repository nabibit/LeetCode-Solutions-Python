# Problem: 36. Valid Sudoku
# Difficulty: Medium
# Link: https://leetcode.com/problems/valid-sudoku/description

# Time Complexity: O(1) - The board size is strictly fixed at 9x9. We iterate exactly 81 times, making the time complexity mathematically constant. (O(N^2) if the board could scale).
# Space Complexity: O(1) - We store at most 81 elements across our Hash Sets, making the auxiliary space strictly bounded and constant.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize our 3 "clipboards" (Hash Sets)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Single pass through the 9x9 grid
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Ignore empty cells
                if val == '.':
                    continue
                    
                # Calculate which of the 9 sub-boxes (0-8) this cell belongs to
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Validation Check! 
                # If we've seen this number in this row, col, or box before -> Invalid!
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                    
                # Record the number on our clipboards for future checks
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        # If we checked every filled cell and found no duplicates, it's valid
        return True

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid Board
    board1 = [
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
    print(f"Test 1: {sol.isValidSudoku(board1)}") 
    # Expected: True
    
    # Test 2: Invalid Board (Duplicate '8' in the top-left 3x3 box)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(f"Test 2: {sol.isValidSudoku(board2)}") 
    # Expected: False