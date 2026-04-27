# Problem: 1391. Check if There is a Valid Path in a Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description

# Time Complexity: O(M * N) - In the worst case, we visit every cell in the grid exactly once.
# Space Complexity: O(M * N) - We store a visited set and a queue that can grow up to the size of the grid.

from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Deine directional vectors
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

        # Define which directions we are allowed to exit our current cell
        exists = {
            1: [LEFT, RIGHT],
            2: [UP, DOWN],
            3: [LEFT, DOWN],
            4: [RIGHT, DOWN],
            5: [LEFT, UP],
            6: [RIGHT, UP]
        }

        # Define which pipes are allowed to ACCEPT our entry from a specific direction
        # Example: If we move RIGHT, the target pipes MUST have a LEFT opening (1, 3, or 5)
        valid_entries = {
            UP: [2, 3, 4], # Moving UP means target must connect DOWN
            DOWN: [2, 5, 6], # Moving DOWN means target must connect UP
            LEFT: [1, 4, 6], # Moving LEFT means target must connect RIGHT
            RIGHT: [1, 3, 5] # Moving RIGHT means target must connect LEFT
        }

        # Standard BFS Setup
        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            r, c = queue.popleft()

            # If we reached the bottom-right corner, we win
            if r == m - 1 and c == n - 1:
                return True

            current_pipe = grid[r][c]

            # Look for all possible exists for the pipe we are currently standing on
            for dr, dc in exists[current_pipe]:
                nr, nc = r + dr, c + dc

                # Check if the next cell is within bounds and hasn't been visited yet
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    next_pipe = grid[nr][nc]
                    # The Handshake Rule: Does the next pipe actually accept water from our direction
                    if next_pipe in valid_entries[(dr, dc)]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return False
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: A perfect path exists
    grid1 = [[2,4,3],[6,5,2]]
    print(f"Test 1: {sol.hasValidPath(grid1)}") 
    # Expected: True
    
    # Test 2: The pipes don't line up (Handshake fails)
    grid2 = [[1,2,1],[1,2,1]]
    print(f"Test 2: {sol.hasValidPath(grid2)}") 
    # Expected: False
    
    # Test 3: 1x1 Grid (Start and End are the same cell)
    grid3 = [[1]]
    print(f"Test 3: {sol.hasValidPath(grid3)}") 
    # Expected: True