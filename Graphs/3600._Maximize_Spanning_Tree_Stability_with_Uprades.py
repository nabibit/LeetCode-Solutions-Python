# Problem: 3600. Maximize Spanning Tree Stability with Upgrades
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

# Time Complexity: O(E * log(Max_Strength) * alpha(V)) - We binary search the possible stability range, performing a nearly linear DSU validation at each step.
# Space Complexity: O(V + E) - We store the DSU parent arrays and filter the edge lists.

from typing import List

class DSU:
    def __init__(self, n: int):
        # Every node starts as its own parent (its own independent component)
        self.parent = list(range(n))
        self.components = n

    def find(self, i: int) -> int:
        # Path compression: Attach the node directly to the root for O(1) future lookups
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        # Connect two nodes. Returns True if a new connection was made, False if they were already connected (a cycle).
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

class Solution:
    def maximizeStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Phase 1: Upfront Impossibility Checks
        dsu_all = DSU(n)
        dsu_must = DSU(n)
        
        mandatory = []
        optional = []
        
        for u, v, s, must in edges:
            dsu_all.union(u, v)
            if must == 1:
                mandatory.append((u, v, s))
                # If mandatory edges form a cycle, a valid spanning tree is mathematically impossible
                if not dsu_must.union(u, v):
                    return -1
            else:
                optional.append((u, v, s))
                
        # If the graph cannot be fully connected even with all possible edges, abort
        if dsu_all.components > 1:
            return -1
            
        # Phase 2: Binary Search on the Answer
        low = 0
        high = max((s * 2 if must == 0 else s) for u, v, s, must in edges)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            dsu = DSU(n)
            possible = True
            
            # Step 1: Add all mandatory edges. They MUST meet the target stability (mid).
            for u, v, s in mandatory:
                if s < mid:
                    possible = False
                    break
                dsu.union(u, v)
                
            if not possible:
                high = mid - 1
                continue
                
            # Step 2: Add "Free" optional edges (strength >= mid naturally)
            upgradable = []
            for u, v, s in optional:
                if s >= mid:
                    dsu.union(u, v)
                elif s * 2 >= mid:
                    upgradable.append((u, v))
                    
            # Step 3: Add "Upgradable" optional edges, keeping track of our budget
            upgrades_used = 0
            for u, v in upgradable:
                # We only use an upgrade if this edge actually connects isolated components
                if dsu.find(u) != dsu.find(v):
                    dsu.union(u, v)
                    upgrades_used += 1
                    if upgrades_used > k:
                        break
                        
            # Step 4: Validate if we formed a full spanning tree within budget
            if dsu.components == 1 and upgrades_used <= k:
                ans = mid       # This stability is possible! Save it.
                low = mid + 1   # Try to find an even higher stability!
            else:
                high = mid - 1  # We couldn't connect it or blew the budget, lower the target.
                
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple graph with 1 upgrade allowed
    edges1 = [[0, 1, 3, 0], [1, 2, 4, 0], [0, 2, 5, 0]]
    print(f"Test 1: {sol.maximizeStability(3, edges1, 1)}") # Expected: 5