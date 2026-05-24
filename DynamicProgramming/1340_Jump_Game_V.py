# Problem: 1340. Jump Game V
# Difficulty: Hard
# Link: https://leetcode.com/problems/jump-game-v/description

# Time Complexity: O(N * d) - For each of the N indices, we look at most 'd' steps to the left and 'd' steps to the right. Because of memoization, each state is computed exactly once.
# Space Complexity: O(N) - We store a memoization array/dictionary of size N, and the recursion stack can go up to N deep in the worst case.

from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        # dp[i] will store the maximum number of indices visited starting from index i
        dp = {}
        
        def dfs(i: int) -> int:
            # If we've already calculated the max jumps from this building, return it
            if i in dp:
                return dp[i]
                
            # A building can always at least visit itself (1 visit)
            max_visits = 1
            
            # Look RIGHT up to 'd' steps
            for x in range(1, d + 1):
                if i + x < n:
                    # If the building blocks our line of sight, we cannot jump over it!
                    if arr[i + x] >= arr[i]:
                        break
                    # If it's valid, simulate the jump and tally the score
                    max_visits = max(max_visits, 1 + dfs(i + x))
                else:
                    break
                    
            # Look LEFT up to 'd' steps
            for x in range(1, d + 1):
                if i - x >= 0:
                    # If the building blocks our line of sight, we cannot jump over it!
                    if arr[i - x] >= arr[i]:
                        break
                    # If it's valid, simulate the jump and tally the score
                    max_visits = max(max_visits, 1 + dfs(i - x))
                else:
                    break
                    
            # Memoize and return
            dp[i] = max_visits
            return max_visits
            
        # The problem allows us to start from ANY index.
        # We simulate starting from every single building and take the absolute maximum.
        return max(dfs(i) for i in range(n))

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard constrained jumping
    print(f"Test 1: {sol.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2)}") 
    # Expected: 4
    # (Optimal path: Start at 10 -> jump to 9 -> jump to 8 -> jump to 6)
    
    # Test 2: Flat line (Cannot jump anywhere!)
    print(f"Test 2: {sol.maxJumps([3,3,3,3,3], 3)}") 
    # Expected: 1
    # (Since you can only jump to STRICTLY smaller buildings, you are trapped)
    
    # Test 3: Staircase (d=1)
    print(f"Test 3: {sol.maxJumps([7,6,5,4,3,2,1], 1)}") 
    # Expected: 7
    # (Start at 7, jump down one step at a time all the way to 1)