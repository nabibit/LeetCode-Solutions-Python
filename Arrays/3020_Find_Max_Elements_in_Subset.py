# Problem: 3020. Find the Maximum Number of Elements in Subset
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description

# Time Complexity: O(N) - We count frequencies in O(N). The squaring loop runs at most O(log(log(Max_Value))) times per unique element, which is practically instant (< 6 operations).
# Space Complexity: O(N) - We store unique element counts in a Hash Map.

from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        # Base Case: The smallest valid mountain peak is just any single number (length 1)
        max_len = 1
        
        # SPECIAL TRAP: Base 1
        # 1 squared is always 1. We can use as many 1s as we have, but the total length 
        # of a valid mountain pattern MUST be an odd number.
        if 1 in freq:
            count_ones = freq[1]
            if count_ones % 2 == 0:
                count_ones -= 1  # Step down to the nearest odd number
            max_len = max(max_len, count_ones)
            del freq[1]  # Remove 1 so our squaring loop below doesn't get stuck forever
            
        # STANDARD BASE SQUARING
        for num in freq:
            curr_len = 0
            curr = num
            
            # Keep climbing as long as we have at least 2 copies of the current stone
            while freq[curr] >= 2:
                curr_len += 2
                curr = curr * curr
                
            # If we successfully found a single copy of the next squared number, it crowns our peak
            if freq[curr] >= 1:
                curr_len += 1
            else:
                # We ran out of stones. We must sacrifice one copy of our last valid pair 
                # to act as the single peak. (e.g., length 6 becomes length 5)
                curr_len -= 1
                
            max_len = max(max_len, curr_len)
            
        return max_len

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Mountain [2, 4, 16, 4, 2]
    print(f"Test 1: {sol.maximumLength([5, 4, 1, 2, 2, 16, 4])}") 
    # Expected: 5
    
    # Test 2: The Base 1 Trap
    print(f"Test 2: {sol.maximumLength([1, 1, 1, 1, 1, 1])}") 
    # Expected: 5 (Uses five 1s to make [1, 1, 1, 1, 1])
    
    # Test 3: No valid pairs exist
    print(f"Test 3: {sol.maximumLength([2, 3, 4, 5])}") 
    # Expected: 1 (Any single element stands alone as a peak)