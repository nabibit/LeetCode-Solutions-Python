# Problem: 2913. Subarrays Distinct Element Sum of Squares I
# Difficulty: Easy
# Link: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

# Time Complexity: O(N^2) - We utilize nested loops to explore all subarrays. Adding to the Hash Set and retrieving its length are O(1) operations.
# Space Complexity: O(N) - The Hash Set stores at most N distinct elements in the worst-case scenario (an array with entirely unique numbers).

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Step 1: Anchor the left boundary of the subarray
        for i in range(n):
            seen = set()
            
            # Step 2: Continuously expand the right boundary
            for j in range(i, n):
                # The set natively absorbs duplicates, keeping our distinct count perfect
                seen.add(nums[j])
                
                # Step 3: Extract the unique count, square it, and accumulate
                count = len(seen)
                total_sum += count * count
                
        return total_sum

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Array with duplicates
    print(f"Test 1: {sol.sumCounts([1, 2, 1])}") 
    # Expected: 15 
    # Subarrays: 
    # [1] -> 1^2 = 1
    # [2] -> 1^2 = 1
    # [1] -> 1^2 = 1
    # [1,2] -> 2^2 = 4
    # [2,1] -> 2^2 = 4
    # [1,2,1] -> 2^2 = 4 (only 1 and 2 are distinct)
    # Total = 15
    
    # Test 2: All identical elements
    print(f"Test 2: {sol.sumCounts([2, 2])}") 
    # Expected: 3
    # Subarrays: [2]->1, [2]->1, [2,2]->1. Total = 3