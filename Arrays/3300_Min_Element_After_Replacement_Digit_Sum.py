# Problem: 3300. Minimum Element After Replacement With Digit Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description

# Time Complexity: O(N * D) - Where N is the number of elements and D is the maximum number of digits in an element. Since D is very small, this is effectively O(N).
# Space Complexity: O(1) - We only store a few integer variables, requiring no extra memory allocations.

from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')

        for num in nums:
            curr_sum = 0

            # Mathamtically extract and sum each digit
            while num > 0:
                curr_sum += num % 10 # Grab the last digit
                num //= 10 # Chop off the last digit

            # Track the smallest digit sum seen so far
            if curr_sum < min_sum:
                min_sum = curr_sum

        return min_sum
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard replacement
    print(f"Test 1: {sol.minElement([10, 12, 13, 14])}") 
    # Expected: 1 (Sums are 1, 3, 4, 5. Min is 1)
    
    # Test 2: Double digit sums
    print(f"Test 2: {sol.minElement([1, 2, 3, 4])}") 
    # Expected: 1 (Sums are 1, 2, 3, 4. Min is 1)
    
    # Test 3: Larger numbers
    print(f"Test 3: {sol.minElement([999, 19, 199])}") 
    # Expected: 10 (Sums are 27, 10, 19. Min is 10)