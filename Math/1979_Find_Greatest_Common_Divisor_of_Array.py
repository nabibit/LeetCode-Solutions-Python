# Problem: 1979. Find Greatest Common Divisor of Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description

# Time Complexity: O(N) - Finding the min and max takes O(N) time. The math.gcd operation takes O(log(min(a, b))) time, which is practically instant.
# Space Complexity: O(1) - We only store two integer variables in auxiliary memory.

import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find the smallest and largest numbers in O(N) time without sorting
        smallest = min(nums)
        largest = max(nums)

        # Use Python's bult-in Euclidean algorithm in C to get the GCD
        return math.gcd(smallest, largest)
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard mix
    print(f"Test 1: {sol.findGCD([2, 5, 6, 9, 10])}") 
    # Expected: 2 (min = 2, max = 10, GCD of 2 and 10 is 2)
    
    # Test 2: Coprime min and max
    print(f"Test 2: {sol.findGCD([7, 5, 6, 8, 3])}") 
    # Expected: 1 (min = 3, max = 8, GCD of 3 and 8 is 1)
    
    # Test 3: Same min and max
    print(f"Test 3: {sol.findGCD([3, 3])}") 
    # Expected: 3 (min = 3, max = 3, GCD is 3)