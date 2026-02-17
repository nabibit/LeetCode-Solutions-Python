# Problem: 3010. Divide an Array Into Subarrays With Minimum Cost I
# Difficulty: Easy
# Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

# Time Complexity: O(N log N) - We sort the slice of the array which takes O(N log N) time 
# (Can be O(N) if we just scan for 2 smallest, but N is usually small here)
# Space Complexity: O(N) - We create the slice nums[1:]

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # The first element is always the starting point of the first subarray, so we take it as is.
        # We need to find 2 more strating points from the remaining elements 
        # to form a total of 3 subarrays
        # To minimize the sum, we simply pick the two smallest elements from nums[1:]
        
        # Isolate the canddates (everything after first element)
        candidates = nums[1:]

        # Sort them to find the smallest values easily
        candidates.sort()

        # Sum = First element + Smallest candidate + Second smallest candidate
        return nums[0] + candidates[0] + candidates[1]
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # [1, 2, 3, 12] -> Split [1], [2], [3, 12]. Costs: 1 + 2 + 3 = 6
    nums1 = [1, 2, 3, 12]
    expected_1 = 6
    result_1 = solution.minimumCost(nums1)
    print(f"Test 1: {result_1 == expected_1} | Got: {result_1} | Expected: {expected_1}")

    # Test Case 2
    # [5, 4, 3] -> Split [5], [4], [3]. Costs: 5 + 4 + 3 = 12
    nums2 = [5, 4, 3]
    expected_2 = 12
    result_2 = solution.minimumCost(nums2)
    print(f"Test 2: {result_2 == expected_2} | Got: {result_2} | Expected: {expected_2}")

    # Test Case 3
    # [10, 3, 1, 1] -> Split [10], [1], [1]. Costs: 10 + 1 + 1 = 12
    # Smallest in rest are 1 and 1.
    nums3 = [10, 3, 1, 1]
    expected_3 = 12
    result_3 = solution.minimumCost(nums3)
    print(f"Test 3: {result_3 == expected_3} | Got: {result_3} | Expected: {expected_3}")