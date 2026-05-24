# Problem: 3660. Jump Game IX
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game-ix/description

# Time Complexity: O(n) - We iterate through the array twice (one forward pass, one backward pass)
# Space Complexity: O(N) - We use an array pf size n to store the prefix maximums and the answer array

from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pre_max = [0] * n

        # Precompute the maximum values from left to right (Prefix Max)
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        # Traverse from right to left tracking the Suffix Min
        suf_min = float('inf')

        for i in range(n - 1, -1, -1):
            # If our maximum available value on the left is greater than the minimum
            # available value on the right, we can bridge to the right side's network 
            if pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                # Otherwise, we are capped at the maximum value on our left
                ans[i] = pre_max[i]

            # Update the suffix minimum for the next iteration
            suf_min = min(suf_min, nums[i])

        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Mixed valley
    nums1 = [2, 4, 1, 3]
    print(f"Test 1: {solution.maxValue(nums1)}")
    # Expected: [4, 4, 4, 4]
    
    # Test Case 2: Strictly decreasing (can always jump backward to the max)
    nums2 = [5, 4, 3, 2, 1]
    print(f"Test 2: {solution.maxValue(nums2)}")
    # Expected: [5, 5, 5, 5, 5]
    
    # Test Case 3: Strictly increasing (trapped, can only reach current max)
    nums3 = [1, 2, 3, 4, 5]
    print(f"Test 3: {solution.maxValue(nums3)}")
    # Expected: [1, 2, 3, 4, 5]