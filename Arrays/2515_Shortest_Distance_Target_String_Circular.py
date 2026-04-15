# Problem: 2515. Shortest Distance to Target String in a Circular Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description

# Time Complexity: O(N) - We scan the array excatly once to find the target strings.
# Space Complexity: O(1) - We only store distance integers.

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')

        for i in range(n):
            if words[i] == target:
                # Calculate the straight-line distance
                straight_dist = abs(i - startIndex)

                # Calculate the wrap-around distance
                wrap_dist = n -straight_dist

                # The actual shortest path to this specific target is the minimum of the two
                shortest_to_this = min(straight_dist, wrap_dist)

                # Update our global minimum distance
                min_distance = min(min_distance, shortest_to_this)

        # If min_distance never changed from infinity, the target wasn't in the array
        return min_distance if min_distance != float('inf') else -1
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Wrap-around is shorter
    print(f"Test 1: {sol.closestTarget(['hello', 'i', 'am', 'leetcode', 'hello'], 'hello', 1)}") 
    # Expected: 1 (Move left from index 1 to index 0)
    
    # Test 2: Straight line is shorter
    print(f"Test 2: {sol.closestTarget(['a', 'b', 'leetcode'], 'leetcode', 0)}") 
    # Expected: 1 (Move left from index 0 wrapping around to index 2)
    
    # Test 3: Target does not exist
    print(f"Test 3: {sol.closestTarget(['i', 'eat', 'leetcode'], 'ate', 0)}") 
    # Expected: -1