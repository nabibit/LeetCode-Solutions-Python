# Problem: 1967. Number of Strings That Appear as Substrings in Word
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description

# Time Complexity: O(P * N) - Where P is the total number of patterns and N is the length of the word. Python's built-in 'in' operator runs at sub-linear speeds in practice.
# Space Complexity: O(1) - We evaluate the conditions on the fly without allocating extra memory structures.

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Python's 'in' operator checks for substrings in highly optimized C code
        # Summing a generator expression evaluates True as 1 and False as 0
        return sum(pattern in word for pattern in patterns)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple matches
    print(f"Test 1: {sol.numOfStrings(['a', 'abc', 'bc', 'd'], 'abc')}") 
    # Expected: 3 ('a', 'abc', and 'bc' are inside 'abc')
    
    # Test 2: Only exact match works
    print(f"Test 2: {sol.numOfStrings(['a', 'b', 'c'], 'aaaaabbbbb')}") 
    # Expected: 2 ('a' and 'b' are present, 'c' is missing)
    
    # Test 3: Zero matches
    print(f"Test 3: {sol.numOfStrings(['a', 'a', 'a'], 'ab')}") 
    # Expected: 3 (Duplicates count separately!)