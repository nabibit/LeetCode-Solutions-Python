# Problem: 3212. Count Submatrices With Equal Frequency of X and Y
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description

# Time Complexity: O(M*N) - We visit every cell in the matrix exactly once
# Space Complexity: O(N) - We optimize space by only trecking the running vertical sums for the columns

from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans =  0

        # Space Optimization: Instead of a full 2D prefix matrix,
        # we only keep track of the cumulative sums dropping down from the columns
        col_x = [0] * cols
        col_y = [0] * cols

        for i in range(rows):
            # We track the running total for the current row as we move left to right
            row_x = 0
            row_y = 0

            for j in range(cols):
                # Add to our horizontal running total
                if grid[i][j] == 'X':
                    row_x += 1
                elif grid[i][j] == 'Y':
                    row_y += 1

                # Add the horizontal row totals to our vertical column totals
                # col_x[j] now represents the total 'X's in the submatrix from (0,0) to (i,j)
                col_x[j] += row_x
                col_y[j] += row_y

                # Check the problem constraints: Equal frequency AND at least one 'X'
                if col_x[j] == col_y[j] and col_x[j] > 0:
                    ans += 1

        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    grid1 = [["X","Y","."],["Y",".","."]]
    print(f"Test 1: {sol.numberOfSubmatrices(grid1)}") # Expected: 3
    
    # Test 2: No submatrix has equal frequencies
    grid2 = [["X","X"],["X","Y"]]
    print(f"Test 2: {sol.numberOfSubmatrices(grid2)}") # Expected: 0
    
    # Test 3: Empty dots
    grid3 = [[".","."],[".","."]]
    print(f"Test 3: {sol.numberOfSubmatrices(grid3)}") # Expected: 0