# Problem: 3488. Closest Equal Element Queries
# Difficulty: Medium
# Link: https://leetcode.com/problems/closest-equal-element-queries/description

# Time Complexity: O(N + Q) - We scan the array of length N once to build our hash map and precalculate distances, the answer Q queries in O(1) time each.
# Space Complexity: O(N) - We store the indices in a hash map and maintain a precalculated answer arrays of size N.
from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # Map to store the sorted occurences of each number: {val: [index1, index2, ...]}
        pos_map = defaultdict(list)

        for i, val in enumerate(nums):
            pos_map[val].append(i)

        # Precompute the minimum distance for every single index in the array
        min_dist = [-1] * n

        for indices in pos_map.values():
            m = len(indices)
            # If the number only appears once, the distance remains -1
            if m > 1:
                for i in range(m):
                    curr_idx = indices[i]

                    # Get the immediate neighbours (wrapping around using modulo and Python's negative index handling)
                    prev_idx = indices[i - 1]
                    next_idx = indices[(i + 1) % m]

                    # Calculate distances on a circular array
                    dist_to_prev = (curr_idx - prev_idx + n) % n
                    dist_to_next = (next_idx - curr_idx + n) % n

                    # Store the shortest path
                    min_dist[curr_idx] = min(dist_to_prev, dist_to_next)

        # Answer all queries instantly using our precomputed lookup table
        return [min_dist[q] for q in queries]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard circular wrapping
    print(f"Test 1: {sol.solveQueries([1, 2, 3, 1], [0, 1, 3])}") 
    # Expected: [1, -1, 1] 
    # (Query 0 is index 0 (val 1). Closest '1' is at index 3. Wrap around distance is 1.)
    # (Query 1 is index 1 (val 2). No other '2', so -1.)
    
    # Test 2: Multiple occurrences
    print(f"Test 2: {sol.solveQueries([5, 5, 5, 5], [2, 0])}") 
    # Expected: [1, 1]