# Problem: 301. Remove Invalid Parentheses
# Difficulty: Hard
# Link: https://leetcode.com/problems/remove-invalid-parentheses/

# Time Complexity: O(2^N) - In the absolute worst-case scenario (e.g., all identical brackets), we could theoretically generate every subsequence of the string.
# Space Complexity: O(2^N) - The Hash Set must store all unique string variations generated at the current BFS level.

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # Helper function to check if a string is perfectly balanced
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    # If we ever have more closing brackets than opening, it's instantly invalid
                    if count < 0:
                        return False
            return count == 0
            
        # Start our BFS with the original string
        current_level = {s}
        
        while True:
            # Check all strings in the current level for validity
            valid_strings = list(filter(is_valid, current_level))
            
            # If we found at least one valid string, we return! 
            # Because we search level-by-level, this guarantees the minimum removals.
            if valid_strings:
                return valid_strings
                
            # If nothing was valid, we generate the next level by removing exactly one character 
            # from every string in our current pool
            next_level = set()
            for string in current_level:
                for i in range(len(string)):
                    # Only try removing parentheses, not letters
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
                        
            # Move down into the next level of the BFS tree
            current_level = next_level

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard removals
    print(f"Test 1: {sol.removeInvalidParentheses('()())()')}") 
    # Expected: ["(())()", "()()()"]
    
    # Test 2: Contains letters (which should not be removed)
    print(f"Test 2: {sol.removeInvalidParentheses('(a)())()')}") 
    # Expected: ["(a())()", "(a)()()"]
    
    # Test 3: Must remove all brackets
    print(f"Test 3: {sol.removeInvalidParentheses(')(')}") 
    # Expected: [""]