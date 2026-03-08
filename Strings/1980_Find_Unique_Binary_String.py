# Problem: 1980. Find Unique Binary String
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-unique-binary-string/description

# Time Complexity: O(N) - We iterate through the array of N strings exactly once
# Space Complexity: O(N) - We store the resulting string characters in a list before joining

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # We will build our unique string character by character
        ans = []

        # We use Cantor's Diagonalization to guarantee uniqueness
        # We iterate through each string at index 'i'
        for i in range(len(nums)):
            # We look at the i-th character of the i-th string
            current_bit = nums [i][i]

            # We flip that character and append it to our answer
            # This guarantees our answer differs from nums[i] at the i-th position
            if current_bit == '0':
                ans.append('1')
            else:
                ans.append('0')

        # We join our array of characters back into a single string
        return "".join(ans)
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: N = 2
    print(f"Test 1: {sol.findDifferentBinaryString(['01','10'])}") # Expected: "11" or "00"
    
    # Test 2: N = 3
    print(f"Test 2: {sol.findDifferentBinaryString(['111','011','001'])}") # Expected: "000" (or other valid)