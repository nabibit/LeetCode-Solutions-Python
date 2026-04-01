# Problem: 3027. Find the Number of Ways to Place People II
# Difficulty: Hard
# Link: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description

# Time Complexity: O(N^2) - We sort the array in O(N log N) and then use a nested loop to sweep all pairs in O(N^2).
# Space Complexity: O(1) - Constant auxiliary space (ignoring Python's TimSort memory overhead).

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points: 
        # Primary: X-coordinate ascending (Left to Right)
        # Secondary: Y-coordinate descending (Top to Bottom)
        # This guarantees that for any j > i, X_j >= X_i
        # If X_j == X_i, then Y_j <= Y_i (Bob will be directly below Alice)
        points.sort(key=lambda p: (p[0], -p[1]))
        
        ans = 0
        n = len(points)
        
        # Iterate every possible Alice
        for i in range(n):
            # We track the highest 'Y' seen so far among points that sit below Alice
            # This 'ceiling' represents the floor of our valid empty rectangles
            max_y_seen = float('-inf')
            
            # Iterate every possible Bob to the right of (or directly below) Alice
            for j in range(i + 1, n):
                
                # Bob must be at or below Alice's Y-coordinate to form a valid bottom-right corner
                if points[j][1] <= points[i][1]:
                    
                    # If Bob is strictly higher than any blocking point we've encountered so far
                    # inside the Alice-Bob bounds, the rectangle is perfectly empty
                    if points[j][1] > max_y_seen:
                        ans += 1
                        
                        # Bob now becomes the new highest blocking point for future sweeps
                        max_y_seen = points[j][1]
                        
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard valid placements
    print(f"Test 1: {sol.numberOfPairs([[1,1],[2,2],[3,3]])}") 
    # Expected: 0 (No valid top-left to bottom-right pairs can be formed without trapping someone)
    
    # Test 2: Diagonal safe zones
    print(f"Test 2: {sol.numberOfPairs([[6,2],[4,4],[2,6]])}") 
    # Expected: 2 (Alice at 2,6 and Bob at 4,4 / Alice at 4,4 and Bob at 6,2)