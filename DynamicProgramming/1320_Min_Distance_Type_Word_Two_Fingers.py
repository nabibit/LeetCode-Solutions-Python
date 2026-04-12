# Problem: 1320. Minimum Distance to Type a Word Using Two Fingers
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description

# Time Complexity: O(N * 27) - N is the length of the word, amd the 'other' finger can be in 27 possible states (A-Z, or Unplaced).
# Space Complexity: O(N * 27) - The maximum number of states stored in our DP cache.

from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Helper function to calculate Manhattan distance on the 6-width keyboard
        def dist(a: int, b: int) -> int:
            if a == 26:
                return 0 # 26 represents a "floating" unplaced finger. Placing it is free
            return abs(a // 6 - b //6) + abs(a % 6 - b % 6)

        # Convert the string into 0-indexed integers (A=0, B=1... Z=25) for easy coordinate math 
        w = [ord(c) - 65 for c in word]

        # dp(i, other) returns the minimum cost to type the rest os the word starting at index i
        # given that one finger is resting on w[i-1], and the other finger on 'other'
        @lru_cache(None)
        def dp(i: int, other: int) -> int:
            # Base Case: We finished typing the whole word
            if i == len(w):
                return 0

            # Option 1: We use the finger that is currently resting on the previous letter
            cost1 = dist(w[i-1], w[i]) + dp(i + 1, other)

            # Option 2: We use the 'other' finger to type the current letter
            # Now, the 'other' finger becomes the one resting on the previous letter!
            cost2 = dist(other, w[i]) + dp(i + 1, w[i-1])
            
            return min(cost1, cost2)

        # The first letter w[0] is typed for free  by our first finger
        # So we start our DP at index 1, with our first finger sitting on w[0],
        # and our 'other' finger floating in the air (state 26).
        ans = dp(1, 26)
        dp.cache_clear() # Clear cache to prevent memory leaks in LeetCode's multi-test environment
        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard typing
    print(f"Test 1: {sol.minimumDistance('CAKE')}") 
    # Expected: 3 
    # (Finger 1 on C, Finger 2 on A (dist 0). Finger 2 moves A->K (dist 2). Finger 1 moves C->E (dist 1). Total 3)
    
    # Test 2: Word requiring lots of hopping
    print(f"Test 2: {sol.minimumDistance('HAPPY')}") 
    # Expected: 6