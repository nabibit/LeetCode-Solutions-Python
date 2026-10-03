# Problem: 32. Longest Valid Parentheses
# Difficulty: Hard
# Link: https://leetcode.com/problems/longest-valid-parentheses/

# Time Complexity: O(N) - We execute exactly two linear sweeps across the string (one forward, one backward).
# Space Complexity: O(1) - We bypass the standard O(N) Stack requirement entirely, maintaining only three integer variables regardless of the input size.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0

        # Step 1: Forward Sweep (left to right)
        # Captures valid sequences and restes on excess closing brackets ')'
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Step 2: Backward Sweep (right to left)
        # Captures sequences bounded by excess opening brackets '(' that the forward sweep missed
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_len
        
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Bounded by excess opening bracket (Caught by Backward Sweep)
    print(f"Test 1: {sol.longestValidParentheses('(()')}") 
    # Expected: 2 
    
    # Test 2: Multiple valid blocks separated by invalid closing brackets
    print(f"Test 2: {sol.longestValidParentheses(')()())')}") 
    # Expected: 4
    
    # Test 3: Empty string
    print(f"Test 3: {sol.longestValidParentheses('')}") 
    # Expected: 0   