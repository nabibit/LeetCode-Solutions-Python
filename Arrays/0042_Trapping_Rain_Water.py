# Problem: 42. Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/description

# Time Complexity: O(N) - We traverse the elevation map exactly once using two pointers moving inward.
# Space Complexity: O(1) - We only store a few integer variables (pointers and max heights), requiring no extra memory.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        # Initialize pointers at the far left and far right ends
        l, r = 0, len(height) - 1
        
        # Track the highest walls seen so far from both directions
        left_max, right_max = height[l], height[r]
        
        water_trapped = 0
        
        # Sweep inward until the pointers collide
        while l < r:
            # Water spills over the shorter wall. We process the side with the smaller max wall!
            if left_max < right_max:
                l += 1
                # Update the highest wall seen on the left
                left_max = max(left_max, height[l])
                # The trapped water is the difference between the highest wall and the current ground level
                water_trapped += left_max - height[l]
            else:
                r -= 1
                # Update the highest wall seen on the right
                right_max = max(right_max, height[r])
                # The trapped water is the difference between the highest wall and the current ground level
                water_trapped += right_max - height[r]
                
        return water_trapped

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard LeetCode Example
    print(f"Test 1: {sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])}") 
    # Expected: 6
    
    # Test 2: Only one massive gap
    print(f"Test 2: {sol.trap([4,2,0,3,2,5])}") 
    # Expected: 9
    
    # Test 3: A flat surface (No water trapped)
    print(f"Test 3: {sol.trap([3,3,3,3])}") 
    # Expected: 0