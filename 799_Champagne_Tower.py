# Problem: 799. Champagne Tower
# Difficulty: Medium
# Link: https://leetcode.com/problems/champagne-tower/description/

# Time Complexity: O(R^2) - Where R is the  query_row. We iterate through the pyramid up to row R
# Space Complexity: O(R) -  We use ONE list that groes to size R. No temp arrays
from typing import List, Optional

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We initialize a fixed buffer for the tower rows
        # Since the max query_row is 99, index 100 is the safety margin
        tower = [0.0] * 101

        # We pour the initial champagne into the top glass (index 0)
        tower[0] = poured

        # We iterate row by row to simulate the flow downwards.
        for r in range(query_row):
            # We iterate backwards from the current row index down to 0
            # This allows us to update the array in-place for the NEXT row
            # without overwriting data we need for the current calculation
            for c in range(r, -1, -1):
                # We calculate the excess liquid in the current glass
                overflow = max(0.0, (tower[c] - 1.0) / 2.0)
                
                # We distribute the overflow to the glass on the right (next row's index c+1)
                # We add to it because it might also receive overflow from its right-side parent later
                tower[c + 1] += overflow
                
                # We update the current index (next row's index c) to become the left child
                # Since we are going backwards, we can safely overwrite this value now
                tower[c] = overflow

        # We return the total liquid in the requested glass, capped at 1.0
        return min(1.0, tower[query_glass])
   
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: 1 cup, row 1, glass 1
    print(solution.champagneTower(1, 1, 1)) # Expected: 0.0
    
    # Test Case 2: 2 cups, row 1, glass 1
    print(solution.champagneTower(2, 1, 1)) # Expected: 0.5 