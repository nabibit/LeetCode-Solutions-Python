# Problem: 2567. Minimum Score by Changing Two Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-score-by-changing-two-elements/

# Time Complexity: O(N log N) - Dominated by sorting the array so we can easily grab the extreme ends.
# Space Complexity: O(1) - Sorting happens in-place (ignoring Timsort's internal buffer), and we just compare three differences.

from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Sort so the smallest and largest values are sitting right at the ends
        nums.sort()
        
        # We can always make the low score 0 by changing our 2 elements to match
        # an existing number. So we just need to minimize the (max - min) gap
        # by testing all 3 ways to chop 2 elements off the ends:
        return min(
            nums[-1] - nums[2],  # Drop the 2 smallest
            nums[-3] - nums[0],  # Drop the 2 largest
            nums[-2] - nums[1]   # Drop 1 from each end
        )

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    print(f"Test 1: {sol.minimizeSum([1, 4, 7, 8, 5])}") 
    # Expected: 3 
    # (Sorted: [1, 4, 5, 7, 8]. Drop 1 and 8 -> [4, 5, 7], gap is 7 - 4 = 3)
    
    # Test 2: Array of length 3 (always 0 since we can make all 3 equal)
    print(f"Test 2: {sol.minimizeSum([1, 4, 3])}") 
    # Expected: 0