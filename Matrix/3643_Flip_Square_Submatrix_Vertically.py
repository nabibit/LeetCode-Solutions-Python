# Problem: 3643. Flip Square Submatrix Vertically
# Difficulty: Easy
# Link: https://leetcode.com/problems/flip-square-submatrix-vertically/description

# Time Complexity: O(K^2) - We iterate through K/2 rows, slicing and swapping K elements each time.
# Space Complexity: O(K) - Python creates temporary lists of size K under the hood during the slice swap.

from typing import List

class Solution:
    def flipSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Set up or two pointers for the top and bottom rows of the target square
        top = x
        bottom = x + k - 1

        # Move inward, swapping the rows until we hit the middle
        while top < bottom:
            # We use slice assignment to swap ONLT the segment of the row inside our square
            # grid[row][strat_col : end_col]
            grid[top][y:y+k], grid[bottom][y:y+k] = grid[bottom][y:y+k], grid[top][y:y+k]

            # Move the pointers closer to the center
            top += 1
            bottom -= 1

        return grid
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: k = 2
    grid1 = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
    # We want to flip a 2x2 square starting at (0, 0)
    print(f"Test 1: {sol.flipSubmatrix(grid1, 0, 0, 2)}") 
    # Expected: [[4, 5, 3], [1, 2, 6], [7, 8, 9]]
    
    # Test 2: k = 1 (A 1x1 square shouldn't change at all)
    grid2 = [[1, 2], [3, 4]]
    print(f"Test 2: {sol.flipSubmatrix(grid2, 1, 1, 1)}") 
    # Expected: [[1, 2], [3, 4]]