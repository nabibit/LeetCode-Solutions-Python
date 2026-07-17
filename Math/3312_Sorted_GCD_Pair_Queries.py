# Problem: 3312. Sorted GCD Pair Queries
# Difficulty: Hard
# Link: https://leetcode.com/problems/sorted-gcd-pair-queries/description

# Time Complexity: O(N + M log M + Q log M) - Where N is the array length, M is the maximum value in nums, and Q is the number of queries. The harmonic series sieve runs in O(M log M).
# Space Complexity: O(M) - We allocate frequency and count arrays bounded strictly by the maximum integer value in nums.

import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Count the exact frequency of every number in the input array
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # Count how many pairs share a GCD that is a MULTIPLE of 'i'
        gcd_cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            # Sum up all occurrences of multiples of 'i' (i, 2i, 3i...)
            multiples_count = 0
            for j in range(i, max_val + 1, i):
                multiples_count += freq[j]
                
            # Combinatorics: Number of ways to pick 2 items from 'multiples_count' items
            gcd_cnt[i] = multiples_count * (multiples_count - 1) // 2
            
        # Inclusion-Exclusion Sieve (Work backward from max_val down to 1)
        # Subtract the exact counts of larger multiples to isolate pairs with EXACTLY GCD 'i'
        for i in range(max_val, 0, -1):
            for j in range(2 * i, max_val + 1, i):
                gcd_cnt[i] -= gcd_cnt[j]
                
        # Build a prefix sum array to map GCDs to their sorted index boundaries
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_cnt[i]
            
        # Answer queries instantly using Binary Search
        ans = []
        for q in queries:
            # bisect_right finds the exact GCD bucket that contains the q-th pair
            ans.append(bisect.bisect_right(prefix_sums, q))
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard constraints
    print(f"Test 1: {sol.gcdValues([2, 3, 4], [0, 2, 2])}") 
    # Expected: [1, 2, 2]
    # (Pairs: (2,3)->GCD 1, (2,4)->GCD 2, (3,4)->GCD 1. Sorted GCDs: [1, 1, 2])
    
    # Test 2: Identical numbers
    print(f"Test 2: {sol.gcdValues([4, 4, 4], [0, 1, 2])}") 
    # Expected: [4, 4, 4]