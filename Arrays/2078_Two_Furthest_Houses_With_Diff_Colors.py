# Problem: 2078. Two Furthest Houses With Different Colors
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-furthest-houses-with-different-colors/description

# Time Complexity: O(N) - We san the array from the edges inward.
# Space Complexity: O(1) - We only store two distance integers.

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len (colors)

        # Scenario 1: Anchor at the first house (index 0)
        # We walk backwards from the end of the street until we find a different color
        dist1 = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors [0]:
                dist1 = i
                break
        
        # Scenario 2: Anchor at the last house (index n - 1)
        # We walk forwards from the start of the street until we find a different color
        dist2 = 0
        for i in range(n):
            if colors[i] != colors[n - 1]:
                dist2 = (n - 1) - i
                break
        
        # The answer is simply the maximum distance found between the two scenarios
        return max(dist1, dist2)
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: First and last houses are already different colors
    print(f"Test 1: {sol.maxDistance([1, 8, 3, 8, 3])}") 
    # Expected: 4 (House 0 is color 1, House 4 is color 3. Distance = 4)
    
    # Test 2: The different color is hidden in the middle
    print(f"Test 2: {sol.maxDistance([1, 1, 1, 6, 1, 1, 1])}") 
    # Expected: 3 (House 0 is color 1, House 3 is color 6. Distance = 3)