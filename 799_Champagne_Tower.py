# Problem: 799. Champagne Tower
# Difficulty: Medium
# Link: https://leetcode.com/problems/champagne-tower/description/

# Time Complexity: O(R^2) - Where R is the  query_row. We iterate through the pyramid up to row R
# Space Complexity: O(1) - The maximum grid is fixed (100x100) based on problem constraints

from typing import List, Optional

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We initialize a 2D grid to simulate the tower
        # We use 102 to handle the 0-100 index safely with a small buffer
        tower = [[0.0] * 102 for _ in range(102)]

        # We pour the initial amount into the top glass
        tower[0][0] = poured
        
        # We iterate through each row to propagate the liquid downwards
        # We only need to process up to query_row
        for r in range(query_row + 1):
            # We iterate through the glasses in the current row
            for c in range(r + 1):
                # We check for overflow
                q = (tower[r][c] - 1.0) / 2.0

                # If there is positive overflow, we distribute it to the next row
                if q > 0:
                    tower[r + 1][c] += q
                    tower[r + 1][c + 1] += q
                    
        # We return the amount in the target glass, capping it at 1.0 since a glass can only hold 1 unit of champagne
        return min(1.0, tower[query_row][query_glass])
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: 1 cup, row 1, glass 1
    print(solution.champagneTower(1, 1, 1)) # Expected: 0.0
    
    # Test Case 2: 2 cups, row 1, glass 1
    print(solution.champagneTower(2, 1, 1)) # Expected: 0.5