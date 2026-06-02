# Problem: 3633. Earliest Finish Time for Land and Water Rides I
# Difficulty: Easy
# Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description

# Time Complexity: O(N * M) - Where N is the number of land rides and M is the number of water rides. We check every combination.
# Space Complexity: O(1) - Constant auxiliary space.

from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        
        min_finish_time = float('inf')
        
        for i in range(n):
            for j in range(m):
                
                # Scenario 1: Ride Land [i] first, then Water [j]
                land_start_1 = landStartTime[i]
                land_end_1 = land_start_1 + landDuration[i]
                water_start_1 = max(land_end_1, waterStartTime[j])
                total_end_1 = water_start_1 + waterDuration[j]
                
                # Scenario 2: Ride Water [j] first, then Land [i]
                water_start_2 = waterStartTime[j]
                water_end_2 = water_start_2 + waterDuration[j]
                land_start_2 = max(water_end_2, landStartTime[i])
                total_end_2 = land_start_2 + landDuration[i]
                
                # Take the best possible outcome for this specific pair
                best_for_pair = min(total_end_1, total_end_2)
                
                # Keep track of the absolute minimum across all pairs
                min_finish_time = min(min_finish_time, best_for_pair)
                
        return min_finish_time

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Staggered starts (Water opens late)
    print(f"Test 1: {sol.earliestFinishTime([10], [5], [15], [5])}") 
    # Expected: 20
    # (Land first: start at 10, finish at 15. Water opens at 15, ride it, finish at 20)
    
    # Test 2: Choosing the best pair
    print(f"Test 2: {sol.earliestFinishTime([1, 10], [5, 2], [5, 2], [3, 10])}") 
    # Expected: 9
    # (Pair (0, 0): Land 0 first (1 to 6). Water 0 opens at 5, start at 6, finish at 9)