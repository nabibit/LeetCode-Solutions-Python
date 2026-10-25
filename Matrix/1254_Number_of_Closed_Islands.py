# Problem: 1254. Number of Closed Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-closed-islands/

# Time Complexity: O(M * N) - We visit every cell in the grid a constant number of times. The DFS flood-fills ensure no cell is processed more than once.
# Space Complexity: O(M * N) - In the worst-case scenario (e.g., a massive snake-like island covering the grid), the recursion call stack could reach O(M * N) depth.

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # Helper function to sink an island (turn 0 to 1)
        def sink_island(r: int, c: int):
            # Base cases: out of bounds or already water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 1:
                return
                
            # Mark the current land cell as water
            grid[r][c] = 1
            
            # DFS in all 4 directions
            sink_island(r + 1, c)
            sink_island(r - 1, c)
            sink_island(r, c + 1)
            sink_island(r, c - 1)
            
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
    # (Two enclosed islands of 0s. The 0s on the right edge are sunk in Phase 1).
    
    # Test 2: Island touching corner
    grid2 = [
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]
    print(f"Test 2: {sol.closedIsland(grid2)}") 
    # Expected: 1
    # (The middle '0' at row 1 col 2 is completely surrounded)