# Problem: 2812. Find the Safest Path in a Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-safest-path-in-a-grid/description

# Time Complexity: O(N^2 log N) - Multi-source BFS takes O(N^2). The Max-Heap processes up to N^2 cells, with heap operations taking O(log(N^2)) which simplifies to O(log N).
# Space Complexity: O(N^2) - We allocate memory for a distance matrix and a visited matrix, plus the BFS queue.

import heapq
from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Base Case: If the start or end cell has a thief, safeness is permanently 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Multi-Source BFS to calculate distance to the nearest thief for every cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # If we haven't visited this cell yet, its shortest distance is curr + 1
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Max-Heap (Dijkstra) to navigate the grid maximizing the minimum safeness
        # Python uses a Min-Heap, so we push negative distances to simulate a Max-Heap
        pq = [(-dist[0][0], 0, 0)] # (-safeness, r, c)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while pq:
            safe, r, c = heapq.heappop(pq)
            safe = -safe # Flip it back to positive
            
            # The moment we reach the end via the Max-Heap, it is mathematically guaranteed 
            # to be the safest possible path.
            if r == n - 1 and c == n - 1:
                return safe
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The safeness of a path is the MINIMUM distance encountered on it
                    min_safe = min(safe, dist[nr][nc])
                    heapq.heappush(pq, (-min_safe, nr, nc))
                    
        return 0

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Single thief in the middle
    print(f"Test 1: {sol.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]])}") 
    # Expected: 2 
    
    # Test 2: Thieves blocking the direct path
    print(f"Test 2: {sol.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])}") 
    # Expected: 2
    
    # Test 3: Thief at the starting line
    print(f"Test 3: {sol.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,0]])}") 
    # Expected: 0