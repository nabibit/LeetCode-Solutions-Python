# Problem: 3761. Minimum Absolute Distance Between Mirror Pairs
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description

# Time Complexity: O(N * D) - Where N is the length of the array, and D is the number of digits. String conversion O(D) which is practically O(1) for standard integers.
# Space Complexity: O(N) - In the worst case, we store a "wanted" value for every element in the array.
from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Dictionary to store the most recent index where a specific "reversed" value is needed
        # Format: seen_needed[target_value] = index_i
        seen_needed = {}
        min_dist = float('inf')

        for j, val in enumerate(nums):
            # Did a previous index put a wanted poster for my exact value?
            if val in seen_needed:
                min_dist = min(min_dist, j - seen_needed[val])

            # Put up my own wanted poster for future numbers to find
            # We calculate the reverse (stripping trailing zeros implicitly by converting back to int)    
            rev_val = int(str(val)[::-1])

            # We overwrite any old poster for this value because we want the most recent index
            # (which guarantees the smallest distance for future matches)
            seen_needed[rev_val] = j

        return min_dist if min_dist != float('inf') else -1
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard mirror pair
    print(f"Test 1: {sol.minMirrorPairDistance([12, 21, 12])}") 
    # Expected: 1 (Index 0 wants 21. Index 1 is 21. Distance: 1 - 0 = 1)
    
    # Test 2: Handling trailing zeros naturally
    print(f"Test 2: {sol.minMirrorPairDistance([120, 5, 21])}") 
    # Expected: 2 (Index 0 wants 21. Index 2 is 21. Distance: 2 - 0 = 2)
    
    # Test 3: No mirror pair exists
    print(f"Test 3: {sol.minMirrorPairDistance([1, 2, 3])}") 
    # Expected: -1