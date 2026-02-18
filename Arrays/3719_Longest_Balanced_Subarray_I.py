# Problem: 3719. Longest Balanced Subarray I
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-balanced-subarray-i/description

# Time Complexity: O(N^2) - We iterate through all the subarrays (nested loops)
# Space Complexity: O(N) - In the worst case, sets store all distinct elements

from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        # We iterate through every index to use it as the staring point of our subarray
        for i in range(n):
            # We initialize sets to track distinct even and odd numbers for the current window
            # Sets automtically handle the "distinct" requirements
            evens = set()
            odds = set()

            # We extend the subarray to the right from the starting point 'i'
            for j in range(i, n):
                val = nums[j] 

                # We categorize the current valiue into even or odd sets
                if val % 2 == 0:
                    evens.add(val)
                else:
                    odds.add(val)

                # We check if the subarray is balanced (equal distinct counts)
                # If balanced, we update the maximum length found so far
                if len(evens) == len(odds):
                    max_len = max(max_len, j - i + 1)

        return max_len
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Mixed numbers
    # Subarray [1, 2, 3, 4] has:
    #   Distinct Odds: {1, 3} (Count: 2)
    #   Distinct Evens: {2, 4} (Count: 2)
    #   Length: 4.
    # Note: [1, 2, 3, 4, 5] fails because distinct odds becomes 3 vs evens 2.
    print(f"Test 1: {solution.longestBalanced([1, 2, 3, 4, 5])}") # Expected: 4
    
    # Test Case 2: Only odd numbers
    # Odds will always be > 0, Evens will always be 0. Never balanced.
    print(f"Test 2: {solution.longestBalanced([1, 1, 1])}") # Expected: 0
    
    # Test Case 3: Repeats
    # Subarray [2, 3, 2, 3] -> Distinct Evens {2} (1), Distinct Odds {3} (1). 1 == 1.
    # Result is the full array length.
    print(f"Test 3: {solution.longestBalanced([2, 3, 2, 3])}") # Expected: 4