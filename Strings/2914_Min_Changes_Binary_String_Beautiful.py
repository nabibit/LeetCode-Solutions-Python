# Problem: 2914. Minimum Number of Changes to Make Binary String Beautiful
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

# Time Complexity: O(N) - We do a single pass through the string, jumping two characters at a time.
# Space Complexity: O(1) - Just a single integer counter, no extra memory needed.

class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        
        # Since every valid substring has to be even length, we can just treat
        # the whole string as a bunch of independent 2-character pairs.
        for i in range(0, len(s), 2):
            # If the pair doesn't match, we only need 1 flip to make it "00" or "11"
            if s[i] != s[i + 1]:
                changes += 1
                
        return changes

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Two mismatched pairs
    print(f"Test 1: {sol.minChanges('1001')}") 
    # Expected: 2 (Pairs are "10" and "01" -> both need 1 flip)
    
    # Test 2: Single mismatched pair
    print(f"Test 2: {sol.minChanges('10')}") 
    # Expected: 1
    
    # Test 3: Already beautiful
    print(f"Test 3: {sol.minChanges('0000')}") 
    # Expected: 0