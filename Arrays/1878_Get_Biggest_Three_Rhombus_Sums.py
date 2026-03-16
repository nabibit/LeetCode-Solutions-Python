# Problem: 1878. Get Biggest Three Rhombus Sums in a Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description

# Time Complexity: O(M * N * min(M,N)) - We visit every cell and expand outwards. The expansion is bound by the grid dimensions.
# Space Complexity: O(U) - Where U is the number of unique sums stored in our set

from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        # We use a set to automatically filter out duplicate sums
        unique_sums = set()

        for i in range(rows):
            for j in range(cols):
                # A single cell is considered a valid rhombus of size 0
                unique_sums.add(grid[i][j])

                # Expand the rhombus size(L) outwards starting from size 1
                L = 1
                while True:
                    # Check if a rhombus of size L can fit ith its top point at (i, j)
                    # The bottom point will be at i + 2*L. The sides extend left and right by L
                    if i + 2 * L >= rows or j - L < 0 or j + L >= cols:
                        break

                    current_sum = 0
                    x, y = i, j

                    # Walk the border: Down-Left
                    for _ in range(L):
                        current_sum += grid[x][y]
                        x += 1
                        y -= 1

                    # Walk the border: Down-Right
                    for _ in range(L):
                        current_sum += grid[x][y]
                        x += 1
                        y += 1

                    # Walk the border: Up-Right
                    for _ in range(L):
                        current_sum += grid[x][y]
                        x -= 1
                        y += 1

                    # Walk the border: Up-Left
                    for _ in range(L):
                        current_sum += grid[x][y]
                        x -= 1
                        y -= 1

                    unique_sums.add(current_sum)
                    L += 1

        # Sort the unique sums in descending order and return the top 3 (or fewer if less than 3 exist)
        return sorted(list(unique_sums), reverse=True)[:3]
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard grid
    grid1 = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
    print(f"Test 1: {sol.getBiggestThree(grid1)}") # Expected: [228, 216, 211]
    
    # Test 2: Small grid with duplicates
    grid2 = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"Test 2: {sol.getBiggestThree(grid2)}") # Expected: [20, 9, 8]