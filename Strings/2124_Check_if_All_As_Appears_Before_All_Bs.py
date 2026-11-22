# Problem: 2124. Check if All A's Appears Before All B's
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# Time Complexity: O(N) - Python scans the string in C under the hood to check for the substring.
# Space Complexity: O(1) - No extra data structures or copies of the string are allocated.

class Solution:
    def checkString(self, s: str) -> bool:
        # If any 'a' shows up after a 'b', the pair "ba" must exist somewhere in s.
        # So as long as "ba" isn't in the string, we're golden.
        return "ba" not in s

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid order
    print(f"Test 1: {sol.checkString('aaabbb')}") 
    # Expected: True
    
    # Test 2: Invalid order ("ba" appears in the middle)
    print(f"Test 2: {sol.checkString('abab')}") 
    # Expected: False
    
    # Test 3: Only 'b's (no 'a's to break the rule)
    print(f"Test 3: {sol.checkString('bbb')}") 
    # Expected: True