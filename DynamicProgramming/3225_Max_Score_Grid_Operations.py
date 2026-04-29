# Problem: 3225. Maximum Score From Grid Operations
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-score-from-grid-operations/description

# Time Complexity: O(N^3) - We iterate through the columns (N), the previous height (N), and the current height (N). The inner loops are flattened using rolling maximums to keep it strictly cubic.
# Space Complexity: O(N^2) - We only need to store the DP state for the current and previous column transitions.

from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0  # A 1x1 grid has no adjacent columns to trigger a score

        # Precompute Prefix Sums for O(1) column interval queries
        # pref[j][k] = sum of the first 'k' elements in column 'j'
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for k in range(n):
                pref[j][k + 1] = pref[j][k] + grid[k][j]

        INF = float('inf')
        
        # dp[p][c] stores the max score up to the current column 'i',
        # where height of col i-1 is 'p', and height of col i is 'c'
        dp = [[-INF] * (n + 1) for _ in range(n + 1)]

        # Initialization for the virtual column before the grid (col -1 has height 0)
        for c in range(n + 1):
            dp[0][c] = 0

        # Process column by column
        for i in range(1, n):
            new_dp = [[-INF] * (n + 1) for _ in range(n + 1)]

            for p in range(n + 1):
                # Calculate the maximums over all possible heights of col i-2 (p_prev)
                max_dp_p = -INF
                for p_prev in range(p + 1):
                    if dp[p_prev][p] > max_dp_p:
                        max_dp_p = dp[p_prev][p]

                global_max_p = max_dp_p
                for M in range(p + 1, n + 1):
                    if dp[M][p] > global_max_p:
                        global_max_p = dp[M][p]

                # Case A: Current column drops or stays flat (c <= p)
                # The right-score intersection is entirely 0, so we just add the left-score!
                if global_max_p != -INF:
                    base_val = global_max_p + pref[i][p]
                    for c in range(p + 1):
                        new_dp[p][c] = base_val - pref[i][c]

                # Case B: Current column rises (c > p)
                # We must carefully apply right-score without double-counting overlaps
                if p < n:
                    term1_max = [-INF] * (n + 1)
                    curr_term1 = max_dp_p - pref[i - 1][p] if max_dp_p != -INF else -INF

                    # Rolling maximum for instances where p_prev is outgrown by 'c'
                    for c in range(p + 1, n + 1):
                        term1_max[c] = curr_term1
                        val_M = dp[c][p]
                        if val_M != -INF:
                            cand = val_M - pref[i - 1][c]
                            if cand > curr_term1:
                                curr_term1 = cand

                    # Rolling maximum for instances where p_prev towers over 'c'
                    term2_max = [-INF] * (n + 1)
                    curr_term2 = -INF
                    for c in range(n, p, -1):
                        val_M = dp[c][p]
                        if val_M > curr_term2:
                            curr_term2 = val_M
                        term2_max[c] = curr_term2

                    # Apply the isolated max configurations
                    for c in range(p + 1, n + 1):
                        ans_c = -INF
                        if term1_max[c] != -INF:
                            ans_c = term1_max[c] + pref[i - 1][c]
                        if term2_max[c] > ans_c:
                            ans_c = term2_max[c]
                        new_dp[p][c] = ans_c

            dp = new_dp

        # The answer is simply the maximum configuration found at the final column
        ans = 0
        for p in range(n + 1):
            for c in range(n + 1):
                if dp[p][c] > ans:
                    ans = dp[p][c]

        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple 2x2 grid
    print(f"Test 1: {sol.maximumScore([[10, 20], [10, 20]])}") 
    # Expected: 40 (Color Col 0 entirely black, leave Col 1 white. Both Col 1 cells touch black.)
    
    # Test 2: 3x3 Valley Formation
    print(f"Test 2: {sol.maximumScore([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}") 
    # Expected: 30 (Color Col 1 entirely black, leave 0 and 2 white. They harvest 12 + 18 respectively.)