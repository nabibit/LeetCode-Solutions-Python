# Problem: 2573. Find the String with LCP
# Difficulty: Hard
# Link: https://leetcode.com/problems/find-the-string-with-lcp/description

# Time Complexity: O(N^2) - We iterate through the N x N matrix to build the string, and iterate through it once more to validate it.
# Space Complexity: O(N) - We store the character array to build the resulting string.

from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        curr_char = 'a'
        
        # 1. Greedy String Construction
        for i in range(n):
            if not word[i]:
                # If we need more than 26 unique characters, it's mathematically impossible
                if curr_char > 'z':
                    return ""
                    
                # Look ahead: Any index 'j' that shares a prefix with 'i' MUST be the exact same character
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = curr_char
                        
                # Move to the next letter in the alphabet for the next discovered unique character
                curr_char = chr(ord(curr_char) + 1)
                
        # 2. DP Validation Auditor
        # We must prove the string we built actually produces the exact LCP matrix given to us
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                # Calculate what the LCP *should* be based on our newly built string
                if word[i] == word[j]:
                    expected_lcp = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected_lcp = 0
                    
                # If reality doesn't match the input matrix, the input matrix is invalid
                if lcp[i][j] != expected_lcp:
                    return ""
                    
        return "".join(word)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid LCP matrix
    print(f"Test 1: {sol.findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]])}") 
    # Expected: "abab"
    
    # Test 2: Invalid LCP matrix (Contradicts itself)
    print(f"Test 2: {sol.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]])}") 
    # Expected: ""