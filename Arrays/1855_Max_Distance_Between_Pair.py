# Problem: 1855. Maximum Distance Between a Pair of Values
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description

# Time Complexity: O(N + M) - We iterate through both arrays at most once using two pointers.
# Space Complexity: O(1) - We only store pointers and a max distance variable.
from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_dist = 0

        # Traverse both arrays simulatenously 
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # Valid pair found. Record the distance and try to push 'j' further
                # to see if we can get an even larger distance
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                # The value in nums2 is too small
                # We must move 'i' forward to find a smaller value in nums1
                i += 1

        return max_dist
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard arrays with a clear maximum distance
    print(f"Test 1: {sol.maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5])}") 
    # Expected: 2 (i = 2 (value 5), j = 4 (value 5). Distance 4 - 2 = 2)
    
    # Test 2: 'j' is forced to stop early
    print(f"Test 2: {sol.maxDistance([2, 2, 2], [10, 10, 1])}") 
    # Expected: 1 (i = 0 (value 2), j = 1 (value 10). Distance 1 - 0 = 1)
    
    # Test 3: No valid pairs possible
    print(f"Test 3: {sol.maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25])}") 
    # Expected: 2 (i = 2 (value 19), j = 4 (value 25). Distance 4 - 2 = 2)