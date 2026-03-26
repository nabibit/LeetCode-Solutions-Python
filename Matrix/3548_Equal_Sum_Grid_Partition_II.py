# Problem: 3548. Equal Sum Grid Partition II
# Difficulty: Hard
# Link: https://leetcode.com/problems/equal-sum-grid-partition-ii/description

# Time Complexity: O(M * N) - We sweep horizontally and vertically exactly once, doing O(1) dictionary lookups
# Space Complexity: O(M * N) - We store the frquencies of the grid elements in Hash Maps

from collections import Counter
from typing import List

class Solution:
    def canPartition(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        # Check Horizontal Cuts
        if m > 1:
            top_counts = Counter()
            bottom_counts = Counter(val for row in grid for val in row)

            s1 = 0
            for r in range(m - 1):
                # Dynamically move row 'r' from the bottom section to the top section
                row_sum = 0
                for val in grid[r]:
                    top_counts[val] += 1
                    bottom_counts[val] -= 1
                    if bottom_counts[val] == 0:
                        del bottom_counts[val]
                    row_sum += val

                s1 += row_sum
                s2 = total_sum - s1

                if s1 == s2:
                    return True
                
                # If top is heavier, can we delete a valid cell from Top to balance it?
                if s1 > s2:
                    diff = s1 - s2
                    if n == 1: # 1D Vertical Grid: Can only remove the top or bottom of the Top section
                        if diff in (grid[0][0], grid[r][0]):
                            return True
                    elif r == 0: # 1D Horizontal Section: Can only remove the left or right ends
                        if diff in (grid[0][0], grid[0][n - 1]):
                            return True
                    else: # 2D Section: We can remove ANY cell in the Top section safely
                        if diff in top_counts:
                            return True
                        
                # If Bottom is heavier, can we delete a valid cell from Bottom to balance it?
                else:
                    diff = s2 - s1
                    if n == 1:
                        if diff in (grid[r + 1][0], grid[m - 1][0]):
                            return True
                    elif r == m - 2:
                        if diff in (grid[m - 1][0], grid[m - 1][n - 1]):
                            return True
                    else:
                        if diff in bottom_counts:
                            return True

        # Check Vertical Cuts
        if n > 1:
            left_counts = Counter()
            right_counts = Counter(val for row in grid for val in row)

            s1 = 0
            for c in range(n - 1):
                # Dynamically move column 'c' from the right section to the left section
                col_sum = 0
                for r in range(m):
                    val = grid[r][c]
                    left_counts[val] += 1
                    right_counts[val] -= 1
                    if right_counts[val] == 0:
                        del right_counts[val]
                    col_sum += val

                s1 += col_sum
                s2 = total_sum - s1

                if s1 == s2:
                    return True

                if s1 > s2:
                    diff = s1 - s2
                    if m == 1:
                        if diff in (grid[0][0], grid[0][c]):
                            return True
                    elif c == 0:
                        if diff in (grid[0][0], grid[m - 1][0]):
                            return True
                    else:
                        if diff in left_counts:
                            return True
                else:
                    diff = s2 - s1
                    if m == 1:
                        if diff in (grid[0][c + 1], grid[0][n - 1]):
                            return True
                    elif c == n - 2:
                        if diff in (grid[0][n - 1], grid[m - 1][n - 1]):
                            return True
                    else:
                        if diff in right_counts:
                            return True

        return False
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: We must delete the '9' at the edge of the top row to make the sums equal
    grid1 = [[9, 2, 2], [1, 1, 2]]
    print(f"Test 1: {sol.canPartition(grid1)}") 
    # Expected: True (Top row sum is 13, bottom is 4. Remove 9 from top end -> 4 == 4)
    
    # Test 2: The '9' breaks the 1D horizontal cut, BUT the 2D vertical cut successfully removes it!
    grid2 = [[2, 9, 2], [1, 1, 2]]
    print(f"Test 2: {sol.canPartition(grid2)}") 
    # Expected: True (Vertical cut leaves Left=[[2,9],[1,1]], Right=[[2],[2]]. Remove 9 from Left -> 4 == 4. Left stays connected!)