# Problem: 2463. Minimum Total Distance Traveled
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-total-distance-traveled/description

# Time Complexity: O(R^2 * F) - R is the number of robots, F is the number of factories. We explore assigning up to R robots at each of the F factories.
# Space Complexity: O(R * F) - We cache the results of our DP states.

from typing import List 
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort both arrays by position to ensure optimal left-to-right matching
        # (Prevents robots from crossing path unnecessarily)
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)

        @lru_cache(None)
        def dp(r_idx: int, f_idx: int) -> int:
            # Base Case 1: All robots have been successfully repaired
            if r_idx == n:
                return 0
            
            # Base Case 2: We ran out of factories but still have broken robots
            if f_idx == m:
                return float('inf')
                
            # Option 1: Skip this factory completely
            min_dist = dp(r_idx, f_idx + 1)
            
            # Option 2: Assign 'k' robots to the current factory (up to its capacity limit)
            curr_dist = 0
            limit = factory[f_idx][1]
            
            for k in range(1, limit + 1):
                if r_idx + k - 1 < n:
                    # Add the walking distance for the newly assigned robot
                    curr_dist += abs(robot[r_idx + k - 1] - factory[f_idx][0])
                    
                    # Calculate the total distance if we assign exactly 'k' robots here 
                    min_dist = min(min_dist, curr_dist + dp(r_idx + k, f_idx + 1))
                else:
                    break # We've successfully assigned all remaining robots
            return min_dist
            
        # Clear the cache before returning to prevent memory leaks across Leetcode test cases
        ans = dp(0, 0)
        dp.cache_clear()
        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard routing
    print(f"Test 1: {sol.minimumTotalDistance([0,4,6], [[2,2],[6,2]])}") 
    # Expected: 4
    # (Robot 0 -> Factory 2 (dist 2). Robot 4 -> Factory 2 (dist 2). Robot 6 -> Factory 6 (dist 0). Total = 4)
    
    # Test 2: Skipping a factory is optimal
    print(f"Test 2: {sol.minimumTotalDistance([1,-1], [[-2,1],[2,1]])}") 
    # Expected: 2
    # (Robot -1 -> Factory -2 (dist 1). Robot 1 -> Factory 2 (dist 1). Total = 2)