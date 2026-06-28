# Problem: 1846. Maximum Element After Decreasing and Rearranging
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description

# Time Complexity: O(N log N) - Dominant operation is sorting the array of N elements.
# Space Complexity: O(N) or O(1) - Python's Timsort takes O(N) auxiliary space under the hood.

from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the bricks from shortest to tallest
        arr.sort()
        
        # The first step of our staircase is strictly forced to be 1
        current_step = 1
        
        # Walk down the rest of the bricks
        for i in range(1, len(arr)):
            # If the brick is taller than our current step, we shave it down 
            # to be exactly 1 unit taller than our staircase so far
            if arr[i] > current_step:
                current_step += 1
                
        return current_step

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard messy gap
    print(f"Test 1: {sol.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1])}") 
    # Expected: 2 (Rearranges to [1, 1, 2, 2, 2])
    
    # Test 2: Massive numbers shaved down
    print(f"Test 2: {sol.maximumElementAfterDecrementingAndRearranging([100, 1, 1000])}") 
    # Expected: 3 (Shaves down to [1, 2, 3])
    
    # Test 3: Already perfect staircase
    print(f"Test 3: {sol.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5])}") 
    # Expected: 5