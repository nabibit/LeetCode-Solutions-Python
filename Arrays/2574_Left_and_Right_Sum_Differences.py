# Problem: 2574. Left and Right Sum Differences
# Difficulty: Easy
# Link: https://leetcode.com/problems/left-and-right-sum-differences/description

# Time Complexity: O(N) - We sum the array once O(N), and then do a single pass O(N).
# Space Complexity: O(N) - We create a new array to store the answers. Auxiliary space is O(1).

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        ans = []
        
        for num in nums:
            # The current number is about to be evaluated, so it leaves the "Right" side
            right_sum -= num
            
            # Calculate the absolute difference between the two running balances
            ans.append(abs(left_sum - right_sum))
            
            # We are stepping past the current number, so it joins the "Left" side
            left_sum += num
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Array
    print(f"Test 1: {sol.leftRightDifference([10, 4, 8, 3])}") 
    # Expected: [15, 1, 11, 22]
    
    # Test 2: Single Element (No left or right neighbors)
    print(f"Test 2: {sol.leftRightDifference([1])}") 
    # Expected: [0]