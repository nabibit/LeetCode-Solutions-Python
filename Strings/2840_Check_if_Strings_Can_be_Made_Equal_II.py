# Problem: 2840. Check if Strings Can be Made Equal With Operations II
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description

# Time Complexity: O(N) - We slice the string and count the character frquencies in a signle linear pass
# Space Complexity: O(1) auxiliary space - The Counter dictionaries will hold a maximum of 26 keys (the lowercase English alphabet), which is constant space

from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Extract the characters at the even indices and count their frequencies
        even_s1 = Counter(s1[::2])
        even_s2 = Counter(s2[::2])

        # Extract the characters at the odd indices and count their frquencies
        odd_s1 = Counter(s1[1::2])
        odd_s2 = Counter(s2[1::2])

        # If both strings have the exact same characters available in their 
        # independent even and odd pools, they can be rearranged to match!
        return even_s1 == even_s2 and odd_s1 == odd_s2
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid string rearrangement
    print(f"Test 1: {sol.checkStrings('abcdba', 'cabdab')}") 
    # Expected: True
    
    # Test 2: Impossible string rearrangement
    print(f"Test 2: {sol.checkStrings('abe', 'bea')}") 
    # Expected: False