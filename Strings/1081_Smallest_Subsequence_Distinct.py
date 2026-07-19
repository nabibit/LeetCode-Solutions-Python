# Problem: 1081. Smallest Subsequence of Distinct Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description

# Time Complexity: O(N) - We iterate through the string once to find last occurrences, and once to build the stack. Each character is pushed and popped at most once.
# Space Complexity: O(1) - The stack and seen set will hold a maximum of 26 characters (the lowercase English alphabet), which is constant space.

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Find the last index where each character appears in the string
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        # 'seen' prevents us from adding duplicate characters to our stack
        seen = set()
        
        for i, char in enumerate(s):
            # If the character is already safely in our stack, ignore it
            if char in seen:
                continue
                
            # The Monotonic Check:
            # - Is there something in the stack?
            # - Is the current character smaller (more alphabetical) than the top of the stack?
            # - Does the top of the stack appear again later in the string?
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                # Kick the larger character out of the stack and remove it from 'seen'
                # so we can grab it again when it appears later!
                popped_char = stack.pop()
                seen.remove(popped_char)
                
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        # The stack now holds our perfect, lexicographically smallest string
        return "".join(stack)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple string
    print(f"Test 1: {sol.smallestSubsequence('bcabc')}") 
    # Expected: "abc"
    
    # Test 2: Complex string with late-occurring unique characters
    print(f"Test 2: {sol.smallestSubsequence('cbacdcbc')}") 
    # Expected: "acdb"