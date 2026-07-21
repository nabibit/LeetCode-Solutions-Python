# Problem: 3499. Maximize Active Section with Trade I
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximize-active-section-with-trade-i/description

# Time Complexity: O(N) - We group and iterate over the string exactly once.
# Space Complexity: O(N) - In the absolute worst case (e.g., "010101"), we store N/2 zero block lengths.

from typing import List
import itertools

class Solution:
    def maximumActiveSection(self, s: str) -> int:
        total_ones = 0
        zero_blocks = []
        
        # Group contiguous identical characters together
        for key, group in itertools.groupby(s):
            length = len(list(group))
            if key == '1':
                # Track the existing '1's that we already have
                total_ones += length
            else:
                # Track the lengths of all the isolated '0' blocks
                zero_blocks.append(length)
                
        # If we don't have at least two '0' blocks, we can't perform a trade that merges them
        if len(zero_blocks) < 2:
            return total_ones
            
        # Find the maximum gain by finding the two largest adjacent '0' blocks
        max_gain = 0
        for i in range(len(zero_blocks) - 1):
            max_gain = max(max_gain, zero_blocks[i] + zero_blocks[i+1])
            
        # The '1' block we sacrificed is perfectly refunded during the trade,
        # so the net addition is exactly the max_gain!
        return total_ones + max_gain

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard trade
    print(f"Test 1: {sol.maximumActiveSection('0100')}") 
    # Expected: 4 
    # (Original '1's = 1. Zero blocks = [1, 2]. Max gain = 1+2 = 3. Total = 4)
    
    # Test 2: Multiple blocks
    print(f"Test 2: {sol.maximumActiveSection('1000100')}") 
    # Expected: 7
    # (Original '1's = 2. Zero blocks = [3, 2]. Max gain = 3+2 = 5. Total = 7)
    
    # Test 3: No valid trades possible
    print(f"Test 3: {sol.maximumActiveSection('111')}") 
    # Expected: 3