# Problem: 3740. Minimum Distance Between Three Equal Elements I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description

# Time Complexity: O(N) - We scan the array exactly once.
# Space Complexity: O(N) - We store at most two indices for each unique number in the array.
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # We only need to store the two most recent indices for each number to calculate the span
        # pos_map[num] = [index_of_occurence_1, index_of_occurence_2]
        pos_map = {}
        min_dist = float('inf')

        for idx, num in enumerate(nums):
            if num not in pos_map:
                pos_map[num] = [idx]
            elif len(pos_map[num]) == 1:
                pos_map[num].append(idx)
            else:
                # We have found a 3rd occurence!
                # The minimum distance for (i, j, k) where i < j < k simplifies to 2 * (k - i)
                i = pos_map[num][0]
                min_dist = min(min_dist, 2 * (idx - i))

                # Slide the window: remove the oldest index, keep the 2nd, add the current 3rd
                pos_map[num] = [pos_map[num][1], idx]

        return min_dist if min_dist != float('inf') else -1
    
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