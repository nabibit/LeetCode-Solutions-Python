# Problem: 1848. Minimum Distance to the Target Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-distance-to-the-target-element/description

# Time Complexity: O(N) - Worst case, the target is at the farthest opposite end of the array. Best case O(1)
# Space Complexity: O(1) - We only store a single distance integer.

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)

        # We check distances starting from 0 and expanding outward
        # The maximum possible distance in the array is n - 1
        for dist in range(n):
            # Check the right side (if within bounds)
            if start + dist < n and nums[start + dist] == target:
                return dist

            # Check the left side (if within bounds)
            if start - dist >= 0 and nums[start - dist] == target:
                return dist

        return 0
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Target is exactly at the start index
    print(f"Test 1: {sol.getMinDistance([1,2,3,4,5], 5, 3)}") 
    # Expected: 1 (Start is index 3 (value 4). Target is 5 at index 4. Distance = 1)
    
    # Test 2: Multiple targets, we want the closest one
    print(f"Test 2: {sol.getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 0)}") 
    # Expected: 0
    
    # Test 3: Expanding outward hits the left side first
    print(f"Test 3: {sol.getMinDistance([1,1,1,10,10,10,10,10,10,10], 1, 9)}") 
    # Expected: 7 (Start is index 9. Target '1' is closest at index 2. Distance = abs(2 - 9) = 7)