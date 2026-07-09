# Problem: 3532. Path Existence Queries in a Graph I
# Difficulty: Medium
# Link: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/description

# Time Complexity: O(N + Q) - We perform a single O(N) linear scan to assign component IDs, then answer Q queries in O(1) constant time each.
# Space Complexity: O(N) - We store the component ID for all N nodes in an auxiliary array.

from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Assign connected components IDs using a linear scan
        comp = [0] * n
        curr_id = 0

        for i in range(n -1):
            # If the gap between adjacent sorted elements exceeds maxDiff,
            # we break the bridge and start a new component block
            if nums[i + 1] - nums[i] > maxDiff:
                curr_id += 1
            comp[i + 1] = curr_id

        # Answer queries instantly in O(1) by checking component ID equality
        return [comp[u] == comp[v] for u, v in queries]
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple disconnected blocks
    print(f"Test 1: {sol.pathExistenceQueries(7, [1, 3, 4, 8, 9, 10, 15], 2, [[0, 2], [1, 5], [3, 5], [2, 6]])}") 
    # Expected: [True, False, True, False]
    # (Components formed: [1, 3, 4] -> id 0, [8, 9, 10] -> id 1, [15] -> id 2)
    
    # Test 2: Everything connected into one giant graph
    print(f"Test 2: {sol.pathExistenceQueries(4, [2, 4, 6, 8], 2, [[0, 3], [1, 2]])}") 
    # Expected: [True, True]