# Problem: 3739. Count Subarrays With Majority Element II
# Difficulty: Hard
# Link: https://leetcode.com/problems/count-subarrays-with-majority-element-ii/description

# Time Complexity: O(N) - We loop through the array exactly once. Each step only does basic addition and subtraction.
# Space Complexity: O(N) - We use a hash map (history_counts) to remember how many times we've visited each specific score.

from typing import List
from collections import defaultdict

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        total_winning_subarrays = 0
        curr_sum = 0        # Our running tug-of-war score
        smaller_count = 0   # How many past moments had a score strictly lower than curr_sum
        
        # history_counts keeps track of how many times we've stood at a specific score.
        # We put {0: 1} because before the game starts, we are standing at score 0 once.
        history_counts = defaultdict(int)
        history_counts[0] = 1
        
        for num in nums:
            if num == target:
                # Our team scored (+1)! We move UP a step
                # All past scores that were tied with our old curr_sum are now below us
                smaller_count += history_counts[curr_sum]
                curr_sum += 1
            else:
                # Enemy team scored (-1)! We move DOWN a step
                # Our new score is curr_sum - 1. Any past moments sitting at this new score 
                # are tied with us now, meaning they are no longer strictly lower
                curr_sum -= 1
                smaller_count -= history_counts[curr_sum]
                
            # Add all strictly lower past moments to our final answer
            total_winning_subarrays += smaller_count
            
            # Record that we are standing at this new score right now
            history_counts[curr_sum] += 1
            
        return total_winning_subarrays

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Given LeetCode Example 1
    print(f"Test 1: {sol.countMajoritySubarrays([1, 2, 2, 3], 2)}") 
    # Expected: 5 (Subarrays dominated by 2)
    
    # Test 2: All elements equal target
    print(f"Test 2: {sol.countMajoritySubarrays([1, 1, 1, 1], 1)}") 
    # Expected: 10 (Every possible subarray wins)
    
    # Test 3: Target missing completely
    print(f"Test 3: {sol.countMajoritySubarrays([1, 2, 3], 4)}") 
    # Expected: 0