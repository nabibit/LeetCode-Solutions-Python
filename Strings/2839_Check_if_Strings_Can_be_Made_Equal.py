# Problem: 2839. Check if Strings Can be Made Equal With Operations I
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description

# Time Complexity: O(1) - The string length is strictly 4, so sorting takes constant time.
# Space Complexity: O(1) - We allocate a few tiny 2-character arrays.

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Separate the string into Even indices (0, 2) and Odd indices (1, 3)
        # Because we can only swap by a distance of 2, these two groups can never mix
        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])

        # Both independent groups must contain the exact same characters
        return even_s1 == even_s2 and odd_s1 == odd_s2
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid swaps possible
    print(f"Test 1: {sol.canBeEqual('abcd', 'cdab')}") 
    # Expected: True (Swap 0 and 2 in s1 -> cbad, then swap 1 and 3 -> cdab)
    
    # Test 2: Impossible to match
    print(f"Test 2: {sol.canBeEqual('abcd', 'dacb')}") 
    # Expected: False