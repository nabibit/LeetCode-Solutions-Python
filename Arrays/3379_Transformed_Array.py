# Problem: 3379. Transformed Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/transformed-array/description/

# Time Complexity: O(N) - We iterate through the array exactly once
# Space Complexity: O(N) - We create a new list  of size N for the result

from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # We use a list comprehension to build the transformed array
        # Note: Using range(n) is faster than enumerate for this case because
        # it avoids the overhead of creating and unpacking tuple objects for every iteration,
        # which is significant when N is small
        # The formula (i + nums[i]) % n handles the circular wrapping for both
        # positive and negative movements automatically
        return [nums[(i + nums[i]) % n] for i in range(n)]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Mixed values
    # Logic: 
    # Index 0 (3) -> moves 3 right -> lands at index 3 -> value is 1
    # Index 1 (-2) -> moves 2 left -> lands at index 3 -> value is 1
    # Index 2 (1) -> moves 1 right -> lands at index 3 -> value is 1
    # Index 3 (1) -> moves 1 right -> lands at index 0 -> value is 3
    test_nums = [3, -2, 1, 1]
    expected_1 = [1, 1, 1, 3]
    result_1 = solution.constructTransformedArray(test_nums)
    print(f"Test 1: {result_1 == expected_1} | Got: {result_1} | Expected: {expected_1}")

    # Test Case 2: Zero movement
    # All zeros mean no movement, so the array stays exactly the same.
    test_zeros = [0, 0, 0]
    expected_2 = [0, 0, 0]
    result_2 = solution.constructTransformedArray(test_zeros)
    print(f"Test 2: {result_2 == expected_2} | Got: {result_2} | Expected: {expected_2}")

    # Test Case 3: Large Wrap Around
    # 4 moves 10 steps right. 10 % 2 = 0 steps effectively. Lands on itself.
    test_wrap = [-10, 10]
    expected_3 = [-10, -10] # Both land on index 0 (value -10)
    result_3 = solution.constructTransformedArray(test_wrap)
    print(f"Test 3: {result_3 == expected_3} | Got: {result_3} | Expected: {expected_3}")