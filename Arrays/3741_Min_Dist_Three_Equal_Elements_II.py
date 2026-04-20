# Problem: 3741. Minimum Distance Between Three Equal Elements II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description

# Time Complexity: O(N) - We iterate through the array once and perform O(1) hash map operations.
# Space Complexity: O(N) - In the worst case, we store all indices of all numbers in the hash map.
from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Map to store the indices of each number encountered
        index_map = defaultdict(list)
        min_span = float('inf')

        for idx, val in enumerate(nums):
            index_map[val].append(idx)

            # If we have at least 3 occurences of the same number
            if len(index_map[val]) >= 3:
                # The minimum distance for (i,j,k) where i < j < k is 2* (k - i)
                # k is the current index, i is the index two positions back in our list
                first_idx = index_map[val][-3]
                current_span = 2*(idx-first_idx)
                min_span = min(min_span, current_span)
        return min_span if min_span != float('inf') else -1
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple groups, find the tightest one
    print(f"Test 1: {sol.minimumDistance([1, 2, 1, 3, 1])}") 
    # Expected: 8 (Indices 0, 2, 4 of '1'. Distance = 2 * (4 - 0) = 8)
    
    # Test 2: Tight group of 3
    print(f"Test 2: {sol.minimumDistance([1, 1, 1])}") 
    # Expected: 4 (Distance = 2 * (2 - 0) = 4)
    
    # Test 3: No good tuple
    print(f"Test 3: {sol.minimumDistance([1, 2, 1, 2])}") 
    # Expected: -1