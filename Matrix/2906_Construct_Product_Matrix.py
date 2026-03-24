# Problem: 2906. Construct Product Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/construct-product-matrix/description

# Time Complexity: O(N * M) - We do exactly two sweeps across the matrix
# Space Complexity: O(1) auxiliary space - We only use a few integer variables. The O(N * M) result matrix does not count towards auxiliary space
from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 12345

        # Initialize our result matrix with zeros
        p = [[0] * cols for _ in range(rows)]

        # Forward Sweep (Prefix Products)
        # We calculate the product of all elements that come BEFORE grid[i][j]
        prefix = 1
        for i in range(rows):
            for j in range(cols):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        # Backwarf Sweep (Suffix Products)
        # We calculate the product of all elements that come AFTER grid[i][j]
        # and multiply it directly into our result matrix
        suffix = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
        return p
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard positive grid
    grid1 = [[1, 2], [3, 4]]
    print(f"Test 1: {sol.constructProductMatrix(grid1)}") 
    # Expected: [[24, 12], [8, 6]]
    
    # Test 2: Grid containing a zero
    grid2 = [[12345, 2], [1, 7]]
    print(f"Test 2: {sol.constructProductMatrix(grid2)}") 
    # Expected: [[14, 0], [0, 0]] (12345 % 12345 == 0)