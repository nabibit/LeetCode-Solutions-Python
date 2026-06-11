# Problem: 3558. Number of Ways to Assign Edge Weights I
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/description

# Time Complexity: O(N) - We perform a single BFS traversal to find the maximum depth of the tree. The exponentiation takes O(log L) time which is negligible.
# Space Complexity: O(N) - We store the tree in an adjacency list and use a queue for the BFS, both taking linear space.

from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Mathematically derive 'n' from the edges array (a tree with N nodes has N-1 edges)
        n = len(edges) + 1
        
        # A tree with 1 node has 0 edges, therefore the path cost is 0 (even)
        if n == 1:
            return 0
            
        # Build the adjacency list for the undirected tree
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Run a BFS to find the maximum depth (longest path from the root)
        max_depth = 0
        
        # Queue stores tuples: (current_node, current_depth, parent_node)
        # Tracking the parent prevents us from infinitely looping backwards!
        queue = deque([(1, 0, -1)])
        
        while queue:
            node, depth, parent = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if neighbor != parent:
                    queue.append((neighbor, depth + 1, node))
                    
        # Total ways to assign 1s and 2s is 2^L. Exactly half of those combinations 
        # result in an odd sum. Therefore, valid ways = 2^(L-1)
        MOD = 10**9 + 7
        
        # pow(base, exp, mod) is highly optimized in Python (runs in O(log exp) time)
        return pow(2, max_depth - 1, MOD)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple chain (1-2-3) -> Max depth is 2.
    print(f"Test 1: {sol.assignEdgeWeights([[1,2],[2,3]])}") 
    # Expected: 2 
    # (Path has 2 edges. To get an odd sum, weights must be [1,2] or [2,1]. That's 2 ways!)
    
    # Test 2: Star graph (Root 1 connected to many leaves) -> Max depth is 1.
    print(f"Test 2: {sol.assignEdgeWeights([[1,2],[1,3],[1,4]])}") 
    # Expected: 1
    # (Path has 1 edge. To get an odd sum, weight must be [1]. That's 1 way!)