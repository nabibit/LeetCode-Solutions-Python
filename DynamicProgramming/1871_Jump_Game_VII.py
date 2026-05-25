# Problem: 1871. Jump Game VII
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game-vii/description

# Time Complexity: O(N) - We iterate through the binary string exactly once. The sliding window update takes O(1) time per step.
# Space Complexity: O(N) - We use a boolean array of size N to track which specific indices are valid launchpads.

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # If the final destionation is '1', we can never land on it
        if s[-1] == '1':
            return False

        n= len(s)
        dp = [False] * n
        dp[0] = True

        # This tracks the number of valid launchpads currently inside our [minJump, maxJump] window
        reachable_in_window = 0

        for i in range(1, n):
            # Add the stone that just entered our minimum jumping range
            if i >= minJump and dp[i - minJump]:
                reachable_in_window += 1

            # Remove the stone that just fell behind our maximum jumping range
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_in_window -= 1

            # If we are standing on a '0' AND there is an active launchpad in our window,
            # this current stone becomes a new valid launchpad!
            if s[i] == '0' and reachable_in_window > 0:
                dp[i] = True

        # Return the very last stone became a valid launchpad
        return dp[-1]
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard valid jumps
    print(f"Test 1: {sol.canReach('011010', 2, 3)}") 
    # Expected: True
    # (Jump 0 -> 3 -> 5)
    
    # Test 2: Trapped by a long sequence of 1s
    print(f"Test 2: {sol.canReach('01101110', 2, 3)}") 
    # Expected: False