# Problem: 3513. Number of Unique XOR Triplets I
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-unique-xor-triplets-i/description

# Time Complexity: O(1) - Because the array is a guaranteed permutation of [1, n], only the length of the array determines the bit-space span.
# Space Complexity: O(1) - No auxiliary memory is required.

from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases: for n < 3, we do not have enough distinct indices to form 0, 
        # so the only achievable values are the original elements themselves ({1} or {1, 2})
        if n < 3:
            return n
            
        # For n >= 3, the triplets completely saturate the entire k-bit vector space,
        # where k is the exact number of bits needed to represent n in binary
        # 1 << k is bitwise equivalent to 2^k!
        return 1 << n.bit_length()

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Given problem example 1 (n = 2)
    print(f"Test 1: {sol.uniqueXorTriplets([1, 2])}") 
    # Expected: 2 (Triplets produce values {1, 2})
    
    # Test 2: Given problem example 2 (n = 3)
    print(f"Test 2: {sol.uniqueXorTriplets([3, 1, 2])}") 
    # Expected: 4 (Triplets produce {0, 1, 2, 3})
    
    # Test 3: Larger permutation (n = 7)
    print(f"Test 3: {sol.uniqueXorTriplets([1, 2, 3, 4, 5, 6, 7])}") 
    # Expected: 8 (Saturates all 3-bit numbers from 0 to 7)