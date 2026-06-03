# Problem: 3635. Earliest Finish Time for Land and Water Rides II
# Difficulty: Medium
# Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/description

# Time Complexity: O(N log N + M log M) - We sort both arrays and perform binary searches, scaling perfectly for massive inputs.
# Space Complexity: O(N + M) - We store zipped tuples and prefix/suffix minimum arrays to cache our best options.

from typing import List
import bisect

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        # Helper function to find the best time assuming we ride 'Category 1' BEFORE 'Category 2'
        def get_best_order_time(starts1, durs1, starts2, durs2):
            n1, n2 = len(starts1), len(starts2)
            
            # Zip and sort the second category by their start times
            rides2 = sorted(zip(starts2, durs2), key=lambda x: x[0])
            starts2_sorted = [r[0] for r in rides2]
            
            # pref_min_dur[i] = Minimum duration of any ride2 from index 0 to i
            pref_min_dur = [float('inf')] * n2
            curr_min = float('inf')
            for i in range(n2):
                curr_min = min(curr_min, rides2[i][1])
                pref_min_dur[i] = curr_min
                
            # suf_min_sum[i] = Minimum (start + duration) of any ride2 from index i to n2-1
            suf_min_sum = [float('inf')] * n2
            curr_min = float('inf')
            for i in range(n2 - 1, -1, -1):
                curr_min = min(curr_min, rides2[i][0] + rides2[i][1])
                suf_min_sum[i] = curr_min
                
            best_time = float('inf')
            
            # Test every ride from Category 1
            for i in range(n1):
                end1 = starts1[i] + durs1[i]
                
                # Binary search to find the split point where Ride 2 starts AFTER Ride 1 ends
                idx = bisect.bisect_left(starts2_sorted, end1)
                
                # Case 1: Ride 2 opens AFTER we finish. We must wait for it to open.
                # We want the ride with the absolute smallest (Start + Duration)
                if idx < n2:
                    best_time = min(best_time, suf_min_sum[idx])
                    
                # Case 2: Ride 2 opened BEFORE we finished. We can jump on immediately!
                # We want the ride with the absolute smallest Duration
                if idx > 0:
                    best_time = min(best_time, end1 + pref_min_dur[idx - 1])
                    
            return best_time

        # Since we can ride them in either order, we test both Land->Water and Water->Land
        ans1 = get_best_order_time(landStartTime, landDuration, waterStartTime, waterDuration)
        ans2 = get_best_order_time(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(ans1, ans2)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Staggered starts (Water opens late)
    print(f"Test 1: {sol.earliestFinishTime([10], [5], [15], [5])}") 
    # Expected: 20
    
    # Test 2: Complex massive choices
    print(f"Test 2: {sol.earliestFinishTime([1, 10], [5, 2], [5, 2], [3, 10])}") 
    # Expected: 9