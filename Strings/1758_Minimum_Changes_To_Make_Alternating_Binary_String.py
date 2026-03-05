# Problem: 1758. Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description

# Time Complexity: O(N) - We scan the string exactly once.
# Space Complexity: O(1) - We only track a single integer counter.

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # We track how many flips it takes to match the "010101..." pattern.
        start_with_zero_flips = 0
        
        for i in range(n):
            # In the "0101..." pattern, even indices are '0' and odd indices are '1'.
            # We use i % 2 to generate the expected integer (0 or 1) for the current position.
            if int(s[i]) != i % 2:
                start_with_zero_flips += 1
                
        # The flips required for the "1010..." pattern is exactly the remaining characters.
        # We simply return the minimum of the two possible patterns.
        return min(start_with_zero_flips, n - start_with_zero_flips)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Needs 1 flip to become "010"
    print(f"Test 1: {sol.minOperations('0100')}") # Expected: 1
    
    # Test 2: Already perfect
    print(f"Test 2: {sol.minOperations('10')}") # Expected: 0
    
    # Test 3: Needs 2 flips to become "1010"
    print(f"Test 3: {sol.minOperations('1111')}") # Expected: 2