# Problem: 3129. Find All Possible Stable Binary Arrays I
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/description

# Time Complexity: O(zero * one) - We fill a 2D DP table with constant time transitions
# Space Complexity: O(zero * one) - We use a 3D array of size (zero+1) x (one+1) x 2

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] represents the number of valid arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] represents the number of valid arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base Cases
        # A sequence of purely 0s is valid if its length is within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
            
        # A sequence of purely 1s is valid if its length is within the limit
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # We build up our combinations from the bottom up
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # To end in a 0, we can append a 0 to ANY valid sequence that is one 0 shorter
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                
                # If we have more 0s than the limit, we must subtract the sequences that 
                # strictly ended in exactly `limit` 0s to avoid exceeding the limit
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]) % MOD
                
                # To end in a 1, we can append a 1 to ANY valid sequence that is one 1 shorter
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                
                # We apply the same subtraction rule for exceeding the 1s limit
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0]) % MOD
                    
        # Our final answer is the sum of valid sequences ending in 0 and ending in 1
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: limit is 2
    print(f"Test 1: {sol.numberOfStableArrays(1, 1, 2)}") # Expected: 2 ("01", "10")
    
    # Test 2: limit is 1
    print(f"Test 2: {sol.numberOfStableArrays(1, 2, 1)}") # Expected: 1 ("101")
    
    # Test 3: limit is 3
    print(f"Test 3: {sol.numberOfStableArrays(3, 3, 2)}") # Expected: 14