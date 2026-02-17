# Problem: [Trionic Array I]
# Difficulty: [Easy]
# Link: [https://leetcode.com/problems/trionic-array-i/description/]

# Time Complexity: O(n) - [We iterate through the array exactly once with the 'i' pointer]
# Space Complexity: O(1) - [We only use a few integer variables (i, n, peak_index) to track our position, no extra lists or maps]

from typing import List, Optional # Import common types

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        # Sanity Check
        # We need at least 4 numbers to make the "Up-Down-Up" shape
        # If it's shorter than that, it's impossible
        if n < 4:
            return False
        
        i = 0

        # First Climb: UP
        # Keep walking forward as long as the next number is bigger
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        # Check if the climb was valid
        # i == 0: We never went up (it started flat or went down immediately)
        # i == n - 1: We climbed all the way to the end (no room left foe down/up)
        if i == 0 or i == n - 1:
            return False
        
        # The descent: DOWN
        # Mark where the peak was so we can check if we actually move down
        peak_index = i

        # Keep walking forward as long as the next number is smaller
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1

        # Check is the descent was valid
        # i == peak_index: We didn't move at all (it went flat or up immediately)
        # i == n - 1: We went down all the way to the end (no room left for the final up)
        if i == peak_index or i == n - 1:
            return False
        
        # Final climb: UP
        # Keep walking forward as long as the next number is bigger
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        # The verdict
        # If we stopped exactly at the last index (n - 1), it means that we completed the pattern
        # If we stopped earlier, it means the pattern broke (like a flat line or a pattern dip)
        return i == n - 1
    
# ---------------------------------------------------
# Optional: Test cases to run locally
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: The perfect Trionic array
    # Up (1->5), Down (5->2), Up (2->8) -> Should be True
    print(f"Test 1: {solution.isTrionic([1, 5, 2, 8])}") 

    # Test Case 2: Just a mountain (Up-Down), missing the final Up
    # Should be False
    print(f"Test 2: {solution.isTrionic([1, 5, 2])}")

    # Test Case 3: Flat line at the start
    # Should be False because it's not strictly increasing
    print(f"Test 3: {solution.isTrionic([1, 1, 5, 2, 8])}")

    # Test Case 4: A valid longer example
    # Up (1->3->5), Down (5->4->2), Up (2->6->9) -> Should be True
    print(f"Test 4: {solution.isTrionic([1, 3, 5, 4, 2, 6, 9])}")