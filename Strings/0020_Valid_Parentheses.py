# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/

# Time Complexity: O(N) - We traverse the string of length N exactly once. Stack push and pop operations execute in O(1) time.
# Space Complexity: O(N) - In the worst-case scenario (e.g., all opening brackets like "((((("), the stack will store all N characters.

class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets directly to their required opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Pop the top element if stack is not empty, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'

                # If the popped bracket doesn't match the expected bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False

            else:
                # It is an opening bracket, push it onte the stack
                stack.append(char)

        # If the stack is empty at the end, all brackets were perfectly matched
        return not stack

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    print(f"Test 1: {sol.isValid('()')}") 
    # Expected: True
    
    print(f"Test 2: {sol.isValid('()[]{}')}") 
    # Expected: True
    
    print(f"Test 3: {sol.isValid('(]')}") 
    # Expected: False
    
    print(f"Test 4: {sol.isValid('([])')}") 
    # Expected: True