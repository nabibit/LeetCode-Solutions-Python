# Problem: 921. Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# Time Complexity: O(N) - We perform a single linear sweep across the string of length N.
# Space Complexity: O(1) - We bypass the standard O(N) Stack requirement entirely, utilizing only two integer counters regardless of string size.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                # We expect a future closing bracket to match this
                close_needed += 1
            else:
                # It's a closing bracket ')'
                if close_needed > 0:
                    # It perfectly matches a previously seen '('
                    close_needed -= 1
                else:
                    # It has no matching '(', so we must artificially add one
                    open_needed += 1
                    
        # Total additions required are the orphaned lefts and orphaned rights
        return open_needed + close_needed

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Needs one of each
    print(f"Test 1: {sol.minAddToMakeValid('())')}") 
    # Expected: 1
    
    # Test 2: Needs all closing brackets
    print(f"Test 2: {sol.minAddToMakeValid('(((')}") 
    # Expected: 3
    
    # Test 3: Perfectly balanced already
    print(f"Test 3: {sol.minAddToMakeValid('()')}") 
    # Expected: 0
    
    # Test 4: Completely inverted
    print(f"Test 4: {sol.minAddToMakeValid(')(')}") 
    # Expected: 2 (Need an open for the first, and a close for the second)