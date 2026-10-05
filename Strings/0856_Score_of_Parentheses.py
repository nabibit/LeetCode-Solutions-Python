# Problem: 856. Score of Parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/score-of-parentheses/

# Time Complexity: O(N) - We perform a single linear sweep across the string of length N.
# Space Complexity: O(1) - We bypass the standard O(N) Stack requirement entirely, utilizing only a depth counter and a total score variable.

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total_score = 0
        depth = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # We are going one layer deeper; future cores will be worth double
                depth += 1
            else:
                # We are stepping out of a layer
                depth -= 1
                
                # If we just closed a core "()" pair, calculate its final scaled value
                if s[i - 1] == '(':
                    # 1 << depth is equivalent to 2^depth
                    total_score += 1 << depth
                    
        return total_score

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple pair
    print(f"Test 1: {sol.scoreOfParentheses('()')}") 
    # Expected: 1
    
    # Test 2: Adjacent pairs (A + B)
    print(f"Test 2: {sol.scoreOfParentheses('()()')}") 
    # Expected: 2 (1 + 1)
    
    # Test 3: Nested pairs (2 * A)
    print(f"Test 3: {sol.scoreOfParentheses('(())')}") 
    # Expected: 2
    
    # Test 4: Complex mixed structure
    print(f"Test 4: {sol.scoreOfParentheses('(()(()))')}") 
    # Expected: 6 
    # Structure: ( () + (()) ) -> 2 * (1 + 2) = 6