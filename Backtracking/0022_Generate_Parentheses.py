# Problem: 22. Generate Parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/generate-parentheses/

# Time Complexity: O(4^n / sqrt(n)) - The time complexity is bounded by the N-th Catalan number, which determines the number of valid parentheses combinations.
# Space Complexity: O(n) - The depth of the recursion stack and the temporary character array both reach a maximum depth of 2n.

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        # Base Case: The combination is complete when it reaches length 2n
        def backtrack(current_string: List[str], open_count: int, close_count: int):

            if len(current_string) == 2 * n:
                ans.append("".join(current_string))
                return

            # Decision 1: Add an open bracket if we have any left
            if open_count < n:
                current_string.append('(')
                backtrack(current_string, open_count + 1, close_count)
                current_string.pop()

            # Decision 2: Add a close bracket if it can match an unclosed open bracket
            if close_count < open_count:
                current_string.append(')')
                backtrack(current_string, open_count, close_count + 1)
                current_string.pop()

        # Start the recursion with an empty string array and 0 counts
        backtrack([], 0, 0)
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard constraints
    print(f"Test 1: {sol.generateParenthesis(3)}") 
    # Expected: ["((()))","(()())","(())()","()(())","()()()"]
    
    # Test 2: Minimal pair
    print(f"Test 2: {sol.generateParenthesis(1)}") 
    # Expected: ["()"]