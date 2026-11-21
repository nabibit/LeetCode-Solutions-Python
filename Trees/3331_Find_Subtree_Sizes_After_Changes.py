# Problem: 3331. Find Subtree Sizes After Changes
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-subtree-sizes-after-changes/

# Time Complexity: O(N) - We build the adjacency list once and visit each node twice (enter/exit) in a single DFS pass.
# Space Complexity: O(N) - Used for the adjacency list, the explicit DFS stack, and the answer array.

from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        # Every node starts with a subtree size of 1 (itself)
        ans = [1] * n
        
        # Tracks the closest ancestor we've seen for each character on the current path
        last_seen = {}
        
        # Explicit stack for iterative DFS to avoid Python's recursion limit on deep trees
        # Tuple format: (node, is_exiting, previous_ancestor_for_this_char)
        stack = [(0, False, -1)]
        
        while stack:
            u, exiting, prev_ancestor = stack.pop()
            char = s[u]
            
            if not exiting:
                # Grab whoever previously held this character above us
                old_ancestor = last_seen.get(char, -1)
                
                # Schedule our exit step so we can restore state and bubble up our size later
                stack.append((u, True, old_ancestor))
                
                # Set ourselves as the new closest ancestor for this character
                last_seen[char] = u
                
                for v in adj[u]:
                    stack.append((v, False, -1))
            else:
                # Backtracking: restore the previous ancestor for this character
                if prev_ancestor == -1:
                    del last_seen[char]
                else:
                    last_seen[char] = prev_ancestor
                    
                # Since any new parent is still an ancestor, we can bubble our final size
                # directly up to it right now without ever rebuilding the tree
                target_parent = prev_ancestor if prev_ancestor != -1 else parent[u]
                if target_parent != -1:
                    ans[target_parent] += ans[u]
                    
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard re-parenting
    print(f"Test 1: {sol.findSubtreeSizes([-1, 0, 0, 1, 1, 1], 'abaabc')}") 
    # Expected: [6, 3, 1, 1, 1, 1]
    
    # Test 2: Re-parenting across multiple levels (2 moves to 1, 4 moves to 0)
    print(f"Test 2: {sol.findSubtreeSizes([-1, 0, 4, 0, 1], 'abbba')}") 
    # Expected: [5, 2, 1, 1, 1]