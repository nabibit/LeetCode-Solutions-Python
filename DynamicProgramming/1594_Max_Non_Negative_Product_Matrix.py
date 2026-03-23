# Problem: 1594. Maximum Non Negative Product in a Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description

# Time Complexity: O(M * N) - We visit every cell in the matrix exactly once to calculate its DP state
# Space Complexity: O(M * N) - We store a tuple of (max, min) for every cell in the grid

from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD =  10**9 + 7

        # dp[i][j] will store a tuple: (max_product, min_product) up to thath cell
        dp = [[(0,0) for _ in range(n)] for _ in range(m)]

        # Base Case: The starting point
        dp[0][0] = (grid[0][0], grid[0][0])

        # Pre-fill the first column (can only come from the above)        
        for i in range(1, m):
            val = dp[i-1][0][0] * grid [i][0]
            dp[i][0] = (val, val)

        # Pre-fill the first row (can only come from the left)
        for j in range(1, n):
            val = dp[0][j-1][0] * grid[0][j]
            dp[0][j] = (val, val)

        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                curr = grid[i][j]

                # Calculate all possible products coming from the Top or the Left
                candidates = (
                    curr * dp[i-1][j][0], # Current * Top Max
                    curr * dp[i-1][j][1], # Current * Top Min
                    curr * dp[i][j-1][0], # Current * Left Min
                    curr * dp[i][j-1][1]  # Current * Left Min 
                )

                # The new state tracks the absolute highest and absolute lowest possible products
                dp[i][j] = (max(candidates), min(candidates))

        # The answer is the maximum product at the bottom-right corner
        max_product = dp[-1][-1][0]

        # If the max product is negative, return -1. Otherwise, return modulo 10^9 + 7
        return max_product % MOD if max_product >= 0 else -1

        

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard path finding a positive product
    grid1 = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
    print(f"Test 1: {sol.maxProductPath(grid1)}") # Expected: -1
    
    # Test 2: Double negatives turning positive
    grid2 = [[1,-2,1],[1,-2,1],[3,-4,1]]
    print(f"Test 2: {sol.maxProductPath(grid2)}") # Expected: 8
    
    # Test 3: Zero wipes out the product
    grid3 = [[1, 3], [0, -4]]
    print(f"Test 3: {sol.maxProductPath(grid3)}") # Expected: 0