# Problem: 3070. Count Submatrices with Top-Left Element and Sum Less Than k
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description

# Time Complexity: O(M*N) worst case, but heavily optimized closer to O(Valide Mtrices + M) using Staircase Pruning
# Space Complexity: O(1) - We calculatre the 2D prefix sum entirely in-place

from typing import List 

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        # We start by assuming we can check every column in the first row
        valid_cols = cols

        for i in range(rows):
            for j in range(valid_cols):
                # Calculate the 2D prefix sum in-place
                top = grid[i-1][j] if i > 0 else 0
                left = grid[i][j-1] if j >0 else 0
                top_left = grid[i-1][j-1] if i > 0 and j > 0 else 0

                # Current cell sum = Area Above + Area Left - Overlapping Top-Left Area + Cell Value
                grid[i][j] += top + left - top_left

                if grid[i][j] <= k:
                    ans += 1

                else:
                    # Staircase Optimizatin:
                    # Because values are non-negative, any cells to the right or below this one
                    # will mathematically HAVE to be > k
                    # We permanently shrink our column boundary for all future rows!
                    valid_cols = j
                    break

        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard matrix
    grid1 = [[7,6,3],[6,6,1]]
    print(f"Test 1: {sol.countSubmatrices(grid1, 18)}") # Expected: 4
    
    # Test 2: Matrix where we hit the limit immediately
    grid2 = [[7,2,9],[1,5,0],[2,4,6]]
    print(f"Test 2: {sol.countSubmatrices(grid2, 6)}") # Expected: 0 (Grid[0][0] > 6)