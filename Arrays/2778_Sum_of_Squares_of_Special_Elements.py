# Problem: 2778. Sum of Squares of Special Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/

# Time Complexity: O(N) - We perform a single linear sweep across the array of length N to check divisibility.
# Space Complexity: O(1) - The generator expression resolves the sum on the fly without allocating an auxiliary array.

from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        # enumerate(nums, 1) gives us 1-based indexing directly
        return sum(num * num for i, num in enumerate(nums, 1) if n % i == 0)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    print(f"Test 1: {sol.sumOfSquares([1,2,3,4])}") 
    # Expected: 21 (Indices 1, 2, 4 are divisors. 1^2 + 2^2 + 4^2 = 21)
    
    # Test 2: Larger array
    print(f"Test 2: {sol.sumOfSquares([2,7,1,19,18,3])}") 
    # Expected: 63 (Indices 1, 2, 3, 6. 2^2 + 7^2 + 1^2 + 3^2 = 63)