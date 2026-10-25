# Problem: 1254. Number of Closed Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-closed-islands/

# Time Complexity: O(M * N) - We visit every cell in the grid a constant number of times. 
# Space Complexity: O(M * N) - The BFS queue will store at most a fraction of the grid cells simultaneously, safely avoiding Python's call stack recursion limits.

from typing import List
from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Helper function to sink an island iteratively (CI/CD safe)
        def sink_island(start_r: int, start_c: int):
            queue = deque([(start_r, start_c)])
            grid[start_r][start_c] = 1 # Mark as water immediately to prevent requeueing
            
            while queue:
                r, c = queue.popleft()
                
                # Check all 4 adjacent directions
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # If it's valid land, sink it and add to the queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
            
        # Step 1: Perimeter Sweep
        # Sink all islands connected to the top and bottom borders
        for c in range(cols):
            if grid[0][c] == 0:
                sink_island(0, c)
            if grid[rows - 1][c] == 0:
                sink_island(rows - 1, c)
                
        # Sink all islands connected to the left and right borders
        for r in range(rows):
            if grid[r][0] == 0:
                sink_island(r, 0)
            if grid[r][cols - 1] == 0:
                sink_island(r, cols - 1)
                
        # Step 2: Interior Sweep
        # Count and sink the remaining strictly enclosed islands
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    sink_island(r, c)
                    
        return closed_islands

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard matrix with closed and open islands
    grid1 = [
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
    ]
    print(f"Test 1: {sol.closedIsland(grid1)}") 
    # Expected: 2 
    
    # Test 2: Island touching corner
    grid2 = [
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]
    print(f"Test 2: {sol.closedIsland(grid2)}") 
    # Expected: 1