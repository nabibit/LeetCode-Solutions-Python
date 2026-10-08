# Problem: 1021. Remove Outermost Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-outermost-parentheses/description/

# Time Complexity: O(N) - We perform a single linear sweep across the string of length N.
# Space Complexity: O(N) - We store the filtered characters in a list before joining them into the final string.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        
        for char in s:
            if char == '(':
                # Only append if it's NOT the outermost opening bracket
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                depth -= 1
                # Only append if it's NOT the outermost closing bracket
                if depth > 0:
                    res.append(char)
                    
        return "".join(res)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard primitive blocks
    print(f"Test 1: {sol.removeOuterParentheses('(()())(())')}") 
    # Expected: "()()()"
    # (Primitives are "(()())" and "(())". Stripping outer gives "()()" + "()" = "()()()")
    
    # Test 2: Highly nested
    print(f"Test 2: {sol.removeOuterParentheses('(()(()))')}") 
    # Expected: "()(())"
    
    # Test 3: Completely flat (all outer shells)
    print(f"Test 3: {sol.removeOuterParentheses('()()')}") 
    # Expected: ""