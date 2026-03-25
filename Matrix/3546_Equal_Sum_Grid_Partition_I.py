# Problem: 3546. Equal Sum Grid Partition I
# Difficulty: Medium
# Link: https://leetcode.com/problems/equal-sum-grid-partition-i/description

# Time Complexity: O(M * N) - We iterate through the grid to calculate the row and column sums
# Space Complexity: O(M + N) - We store the 1D projected sums for the rows and columns

from typing import List

class Solution:
    def canPartition(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        # Projet the 2D grid into 1D row sums and 1D column sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(rows)) for j in range(cols)]

        # Calculate the total sum of the entire grid
        total_sum = sum(row_sums)

        # If the total sum is odd, it is mathematically impossible to split it into two equal integers
        if total_sum % 2 != 0:
            return False
        
        # Check for a valid horizontal cut
        # We stop at 'rows - 1' because the cut must leave at least one row in the bottom section
        target = total_sum // 2

        # Check for a valid vertical cut
        # We stop at 'cols - 1' because the cut must leave at least one colum in the right section
        running_sum = 0
        for i in range(rows - 1):
            running_sum += row_sums[i]
            if running_sum == target:
                return True

        running_sum = 0
        for j in range(cols - 1):
            running_sum += col_sums[j]
            if running_sum == target:
                return True

        return False
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid horizontal cut
    grid1 = [[1, 2], [1, 2]]
    print(f"Test 1: {sol.canPartition(grid1)}") 
    # Expected: True (Top row = 3, Bottom row = 3)
    
    # Test 2: Invalid cut (Odd sum)
    grid2 = [[1, 2, 1], [2, 1, 2]]
    print(f"Test 2: {sol.canPartition(grid2)}") 
    # Expected: False (Total sum is 9, which is odd. Impossible to split evenly.)
    
    # Test 3: Valid vertical cut
    grid3 = [[2, 1, 3], [4, 1, 5]]
    print(f"Test 3: {sol.canPartition(grid3)}") 
    # Expected: True (Col 0 + Col 1 = 8, Col 2 = 8)