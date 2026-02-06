# Problem: 3634. Minimum Removals to Balance Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06

# Time Complexity: O(N log N) - [ Sortting the array dominates the time complexity. The sliding window is linear O(N)
# Space Complexity: O(1) or O(n) - [ Depends on the sorting implementation (Python's built-in sort is Timsort which is O(n) in the worst case, but we can consider it O(1) if we ignore the space used for sorting)]
from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # We sort the array to ensure that for any subarray nums[i...j],
        # nums[i] is the minimum and nums[j] is the maximum
        nums.sort()

        left = 0
        max_kept = 0

        # We iterate through the array, expanding the window with the 'right' pointer
        for right in range(len(nums)):
            # We maintain the balanced condition: max_element <= min_element * k
            # Since the array is sorted, nums[right] is max and nums[left] is min
            # If the condition is violated, we shrink the window from the left
            while left < right and nums[right] > nums[left] * k:
                left += 1

            # We update the maximum number of elemnts er can keep in a valid window
            current_window_size = right - left + 1
            max_kept = max(max_kept, current_window_size)

        # The result is the total number of elements minus the maximum number we can keep in a valid window
        return len(nums) - max_kept
    
# ---------------------------------------------------
# Local Test Area: Edge Cases
if __name__ == "__main__":
    solution = Solution()
    
    print("--- Running Edge Case Tests ---")

    # Edge Case 1: k=0 (Strict equality or zeros)
    # Even if k=0, a single element is always balanced per the prompt note.
    # If nums=[1, 10, 20], we can only keep [1] (or [10], or [20]). Max kept = 1.
    nums1 = [1, 10, 20]
    k1 = 0
    print(f"Test 1 (k=0): Expected 2 removals. Got: {solution.minRemoval(nums1, k1)}")

    # Edge Case 2: Already Balanced
    # Max (4) <= Min (2) * 2 (4). Condition holds for the whole lot.
    nums2 = [2, 3, 4]
    k2 = 2
    print(f"Test 2 (Already Balanced): Expected 0 removals. Got: {solution.minRemoval(nums2, k2)}")

    # Edge Case 3: All Identical Numbers
    # Should keep all of them regardless of k (unless k < 1 and nums > 0, but size 1 rule applies).
    # If k=1, 5 <= 5*1. Valid.
    nums3 = [5, 5, 5, 5]
    k3 = 1
    print(f"Test 3 (Identical): Expected 0 removals. Got: {solution.minRemoval(nums3, k3)}")

    # Edge Case 4: Single Element
    # Must always return 0 removals.
    nums4 = [100]
    k4 = 0
    print(f"Test 4 (Single Element): Expected 0 removals. Got: {solution.minRemoval(nums4, k4)}")

    print("--- Tests Complete ---")