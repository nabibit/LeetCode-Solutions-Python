# Problem: 3418. Maximum Amount of Money Robot Can Earn
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description

# Time Complexity: O(M * N) - We visit every cell in the grid exactly once and perform a constant O(3) state checks
# Space Complexity: O(M * N) - We allocate a 3D DP table of size [M][N][3]. (Can be otpimized to O(N) by only storing the previous row)

from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])

        # dp[r][c][k] stores the max money at cell (r,c) having used exactly 'k' neutralizations
        # We initialize with negative infinity because total coins can fall below zero
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        # Base Case: Starting at (0,0)
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            # We can choose to immediately burn 1 neutralization on the starting cell
            dp[0][0][1] = 0

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                val = coins[r][c]

                # Check transisitons coming from the TOP
                if r > 0:
                    for k in range(3):
                        if dp[r-1][c][k] != -float('inf'):
                            # Option A: Standard move (take the coins or pay the robber)
                            dp[r][c][k] = max(dp[r][c][k], dp[r-1][c][k] + val)

                            # Option B: Use a superpower (only if it's a robber and we have powers left)
                            if val < 0 and k < 2:
                                dp[r][c][k+1] = max(dp[r][c][k+1], dp[r-1][c][k])


                # Check transitions coming from the LEFT
                if c > 0:
                    for k in range(3):
                        if dp[r][c-1][k] != -float('inf'):
                            # Option A: Standard move
                            dp[r][c][k] = max(dp[r][c][k], dp[r][c-1][k] + val)

                            # Option B: Use a superpower
                            if val < 0 and k < 2:
                                dp[r][c][k+1] = max(dp[r][c][k+1], dp[r][c-1][k])

        # The answer is the absolute maximum value we can achieve at the bottom-right corner
        # across all possible universes (using 0,1, or 2 neutralizations)
        return max(dp[m-1][n-1])
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Grid where neutralizing robbers significantly boosts profit
    grid1 = [[0, 1, -1], [1, -2, 3], [2, -3, 4]]
    print(f"Test 1: {sol.maximumAmount(grid1)}") 
    # Expected: 8 (Path: R, R, D, D. Neutralize -1 and -3. Coins: 0 + 1 + 0 + 3 + 0 + 4 = 8)
    
    # Test 2: Grid where we don't need to use all neutralizations
    grid2 = [[10, 10, 10], [10, 10, 10]]
    print(f"Test 2: {sol.maximumAmount(grid2)}") 
    # Expected: 40