# Problem: 678. Valid Parenthesis String
# Difficulty: Medium
# Link: https://leetcode.com/problems/valid-parenthesis-string/

# Time Complexity: O(N) - We execute a single linear pass through the string.
# Space Complexity: O(1) - We maintain exactly two integer variables (low, high), completely avoiding stack allocations or recursive call stacks.

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0 # The minimum possible open left brackets
        high = 0 # The maximum possible open left brackets

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else: # char == '*'
                low -= 1 # Treat '*' as ')'
                high += 1 # Treat '*' as '('

            # If the maximum possible open brackets is negative, we have too many ')'
            if high < 0:
                return False

            # We can't have a negative amount of required open breackets.
            # If low < 0, it just means we treat some '*' as empty strings instead of ')'
            low = max(low, 0)

        # If low is 0, we can succesfully match all brackets
        return low == 0


# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard valid
    print(f"Test 1: {sol.checkValidString('()')}") 
    # Expected: True
    
    # Test 2: Wildcard as empty string
    print(f"Test 2: {sol.checkValidString('(*)')}") 
    # Expected: True
    
    # Test 3: Wildcard as '(' to balance a deficit
    print(f"Test 3: {sol.checkValidString('(*))')}") 
    # Expected: True