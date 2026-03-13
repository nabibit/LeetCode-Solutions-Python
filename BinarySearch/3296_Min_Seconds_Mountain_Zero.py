# Problem: 3296. Minimum Number of Seconds to Make Mountain Height Zero
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description

# Time Complexity: O(N * log(Max_Time)) - We binary search the massive time range, doing an O(1) math check for each worker.
# Space Complexity: O(1) - We only store integer boundaries and accumulators.

import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Helper function to check if 'mid' seconds is enough to level the mountain
        def canLevelMountain(mid: int) -> bool:
            total_reduced = 0
            for w in workerTimes:
                # We need to find the max 'x' such that: w * x * (x + 1) / 2 <= mid
                # This reorganizes into the quadratic equation: x^2 + x - (2 * mid / w) <= 0
                # Using the quadratic formula, we solve for the positive root:
                
                # We use math.isqrt for perfect integer precision avoiding floating point errors
                max_x = (-1 + math.isqrt(1 + (8 * mid) // w)) // 2
                total_reduced += max_x
                
                if total_reduced >= mountainHeight:
                    return True
            return False

        low = 0
        # The absolute worst-case scenario: the fastest worker has to dig the entire mountain alone.
        min_w = min(workerTimes)
        high = min_w * mountainHeight * (mountainHeight + 1) // 2
        
        ans = high
        
        # Binary Search on the Answer
        while low <= high:
            mid = (low + high) // 2
            
            if canLevelMountain(mid):
                ans = mid       # This time works! Save it.
                high = mid - 1  # Try to force them to do it even faster.
            else:
                low = mid + 1   # Not enough time, we need to give them more seconds.
                
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: mountainHeight = 4, workerTimes = [2, 1, 1]
    print(f"Test 1: {sol.minNumberOfSeconds(4, [2, 1, 1])}") # Expected: 3
    
    # Test 2: mountainHeight = 10, workerTimes = [3, 2, 2, 4]
    print(f"Test 2: {sol.minNumberOfSeconds(10, [3, 2, 2, 4])}") # Expected: 12