# Problem: 3130. Find All Possible Stable Binary Arrays II
# Difficulty: Hard
# Link: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/description

# Time Complexity: O(zero * one) - We fill a 2D DP table with O(1) mathematical transitions
# Space Complexity: O(zero * one) - We use two separate arrays to minimize Python overhead
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # We split our states into two separate 2D arrays for faster memory access
        # dp0[i][j] tracks valid arrays with 'i' zeros and 'j' ones, ending with 0
        # dp1[i][j] tracks valid arrays with 'i' zeros and 'j' ones, ending with 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base Cases:  Sequences consisting entirely of a single digit (all 0s or all 1s)
        # are valid only up to the specified 'limit'
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        # We build our valid combinations from the bottom up
        for i in range (1, zero + 1):
            for j in range(1, one + 1):

                # To end in a 0, we take all valid previous sequences and append a 0
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD

                # We mathematically substract the exact number of sequences that just exceeded the 0 limit
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j]) % MOD

                # To end in a 1, we take all valid previous sequences and append a 1
                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD

                # We mathematically substract the exact number of sequences that just exceeded the 1 limit
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1]) % MOD

        # The final answer is the sum of valid sequences that just exceeded the 1 limit
        return (dp0[zero][one] + dp1[zero][one]) % MOD
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: limit is 2
    print(f"Test 1: {sol.numberOfStableArrays(1, 1, 2)}") # Expected: 2
    
    # Test 2: limit is 1
    print(f"Test 2: {sol.numberOfStableArrays(1, 2, 1)}") # Expected: 1
    
    # Test 3: Large constraints test
    print(f"Test 3: {sol.numberOfStableArrays(3, 3, 2)}") # Expected: 14