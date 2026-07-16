# Problem: 3867. Sum of GCD of Formed Pairs
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

# Time Complexity: O(N log N) - We iterate the array in O(N), sort it in O(N log N), and process pairs in O(N). The math.gcd operations take O(log(min(a, b))) which is negligible.
# Space Complexity: O(1) - We mutate the input array in-place, avoiding the O(N) memory allocation for the prefixGcd array.

import math
from typing import List

class Solution:
    def sumOfGcd(self, nums: List[int]) -> int:
        n = len(nums)
        current_max = 0
        
        # Calculate prefix GCDs and overwrite the input array to save space
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            # Replace the number with the GCD of itself and the running maximum
            nums[i] = math.gcd(nums[i], current_max)
            
        # Sort the array in non-decreasing order
        nums.sort()
        
        # Form pairs (smallest, largest) using two pointers
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        # The strictly less-than operator automatically ignores the middle element if N is odd
        while left < right:
            total_gcd_sum += math.gcd(nums[left], nums[right])
            left += 1
            right -= 1
            
        return total_gcd_sum

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Even length array
    print(f"Test 1: {sol.sumOfGcd([4, 8, 2, 6])}") 
    # Expected: 4 
    # (mxi: 4, 8, 8, 8 -> prefixGcd: [4, 8, 2, 2] -> sorted: [2, 2, 4, 8])
    # (Pairs: (2, 8) -> gcd=2, (2, 4) -> gcd=2. Total sum = 4)
    
    # Test 2: Odd length array (middle ignored)
    print(f"Test 2: {sol.sumOfGcd([3, 9, 6])}") 
    # Expected: 3