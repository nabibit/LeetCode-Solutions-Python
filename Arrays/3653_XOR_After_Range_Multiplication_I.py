# Problem: 3653. XOR After Range Multiplication Queries I
# Difficulty: Medium
# Link: https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description

# Time Complexity: O(Q* (N/k)) - In the worst case where k=1,this is O(Q * N). Because Q and N are <= 1000, this peaks at ~1,000,000 operations, which easily passes within the time limit.
# Space Complexity: O(1) - We modify the input array completely in-place.

from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Simulate every query exactly as requested
        for l, r, k, v in queries:
            # We use Python's built-in step size 'k' to effortlessly jump through the array
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD

        # Compute the final XOR of all elements
        ans = 0
        for num in nums:
            ans ^= num


        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard single step size
    print(f"Test 1: {sol.xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]])}") 
    # Expected: 4 (Array becomes [4, 4, 4]. 4 ^ 4 ^ 4 = 4)
    
    # Test 2: Variable step sizes
    print(f"Test 2: {sol.xorAfterQueries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]])}") 
    # Expected: 31