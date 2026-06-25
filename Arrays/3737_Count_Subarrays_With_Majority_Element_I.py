# Problem: 3737. Count Subarrays With Majority Element I
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-subarrays-with-majority-element-i/description

# Time Complexity: O(N) - We iterate through the array exactly once, performing O(1) mathematical updates at each step
# Space Complexity: O(N) - In the worst case, we track up to N unique prefix sums in our Hash Map

from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        curr_sum = 0
        valid_past = 0
        
        # freq tracks how many times we've seen a specific prefix sum
        freq = defaultdict(int)
        freq[0] = 1  # Base case: A prefix sum of 0 exists at the very beginning
        
        for num in nums:
            if num == target:
                # We stepped UP (+1). All sums strictly less than our old curr_sum 
                # are still valid, PLUS all the sums that were equal to curr_sum
                valid_past += freq[curr_sum]
                curr_sum += 1
            else:
                # We stepped DOWN (-1). Our new sum is curr_sum - 1
                # Any past sums that are equal to our NEW sum are no longer strictly less
                curr_sum -= 1
                valid_past -= freq[curr_sum]
                
            ans += valid_past
            freq[curr_sum] += 1
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: The target is 1
    print(f"Test 1: {sol.countSubarrays([1, 1, 2, 1, 3], 1)}") 
    # Expected: 8
    
    # Test 2: Target appears rarely
    print(f"Test 2: {sol.countSubarrays([1, 2, 3], 1)}") 
    # Expected: 1 (Only the subarray [1] works)
    
    # Test 3: Array dominated by target
    print(f"Test 3: {sol.countSubarrays([2, 2, 2], 2)}") 
    # Expected: 6 (Every possible subarray works)