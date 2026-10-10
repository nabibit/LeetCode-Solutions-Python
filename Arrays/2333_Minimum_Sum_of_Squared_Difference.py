# Problem: 2333. Minimum Sum of Squared Difference
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-sum-of-squared-difference/

# Time Complexity: O(N + M) - Where N is the length of the arrays and M is the maximum absolute difference (at most 10^5). We iterate the arrays once to build the frequency map, and iterate the buckets once to exhaust K.
# Space Complexity: O(M) - We allocate a frequency bucket array of size M + 1 to track the distribution of differences.

from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        
        # Step 1: Calculate absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        sum_diffs = sum(diffs)
        
        # If we have enough operations to reduce every difference to 0
        if k >= sum_diffs:
            return 0
            
        # Step 2: Build a frequency map (Bucket Sort) for the differences
        max_diff = max(diffs)
        buckets = [0] * (max_diff + 1)
        for diff in diffs:
            buckets[diff] += 1
            
        # Step 3: Greedily reduce the largest differences
        for d in range(max_diff, 0, -1):
            if k == 0:
                break
                
            if buckets[d] > 0:
                # We can only shift as many elements as we have operations (k)
                # or as many elements as currently exist in this bucket
                shift_count = min(k, buckets[d])
                
                buckets[d] -= shift_count
                buckets[d - 1] += shift_count
                k -= shift_count
                
        # Step 4: Calculate the final sum of squared differences
        return sum(d * d * count for d, count in enumerate(buckets) if count > 0)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard reduction with k = 3
    print(f"Test 1: {sol.minSumSquareDiff([1,2,3,4], [2,10,20,19], 2, 1)}") 
    # Expected: 486
    
    # Test 2: Not enough operations to zero everything (k = 11, sum = 15)
    print(f"Test 2: {sol.minSumSquareDiff([1,4,10,12], [5,8,6,9], 1, 10)}") 
    # Expected: 4
    
    # Test 3: Standard LeetCode Example 1 (k = 0, no reductions)
    print(f"Test 3: {sol.minSumSquareDiff([1,2,3,4], [2,10,20,19], 0, 0)}") 
    # Expected: 579
    
    # Test 4: Enough operations to zero everything (k = 20, sum = 15)
    print(f"Test 4: {sol.minSumSquareDiff([1,4,10,12], [5,8,6,9], 10, 10)}") 
    # Expected: 0