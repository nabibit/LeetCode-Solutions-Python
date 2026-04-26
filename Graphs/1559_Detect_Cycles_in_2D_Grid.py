# Problem: 1559. Detect Cycles in 2D Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/detect-cycles-in-2d-grid/description

# Time Complexity: O(M * N) - We visit each cell in the grid at most once.
# Space Complexity: O(M * N) - We store a global visited set and a queue that can groe up to the size of the grid.

from typing import List
from collections import deque

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # We must check every unvisited cell because the grid might have disconnected islands
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    char = grid[i][j]

                    # Queue stores: (current_row, current_col, parent_row, parent_col)
                    # We initialize the parent as (-1, -1) since the starting cell has no parent
                    queue = deque([(i, j, -1, -1)])
                    visited.add((i, j))

                    while queue:
                        r, c, pr, pc = queue.popleft()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            # Stay within grid bounds
                            # Only walk on the same characters
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == char:
                                # The "Don't Look Back" Rule
                                if (nr, nc) != (pr, pc):

                                    # If the valid neighbour is ALREADY visited, we found a loop
                                    if (nr, nc) in visited:
                                        return True

                                    visited.add((nr, nc))
                                    queue.append((nr, nc, r, c))


        return False
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: A clear cycle exists
    grid1 = [
        ["a","a","a","a"],
        ["a","b","b","a"],
        ["a","b","b","a"],
        ["a","a","a","a"]
    ]
    print(f"Test 1: {sol.containsCycle(grid1)}") 
    # Expected: True (The 'a's form a massive ring around the 'b's)
    
    # Test 2: No cycle, just a dead-end path
    grid2 = [
        ["a","b","b"],
        ["b","z","b"],
        ["b","b","a"]
    ]
    print(f"Test 2: {sol.containsCycle(grid2)}") 
    # Expected: False
    
    # Test 3: Path of length < 4 (Invalid cycle)
    grid3 = [
        ["a","a"],
        ["a","a"]
    ]
    print(f"Test 3: {sol.containsCycle(grid3)}") 
    # Expected: True (A 2x2 block forms a cycle of exactly length 4: (0,0)->(0,1)->(1,1)->(1,0)->(0,0))