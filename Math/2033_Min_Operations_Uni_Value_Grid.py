# Problem: 2033. Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description

# Time Complexity: O(K log K) - Where K is the total number of elements (M * N). We flatten and sort the grid.
# Space Complexity: O(K) - We store the flattened 1D array to find the median.
from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the @D grif into a 1D list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # Sort the array to easily find the median
        nums.sort()
        
        # The remainder that EVERY number must share
        target_mod = nums[0] % x
        
        # In mathematics, the median minimizes the absolute differences
        median = nums[len(nums) // 2]
        
        total_operations = 0
        
        # Calculate the steps required for every number to reach the median
        for num in nums:
            # If the remainder doesn't match, they can neber reach the same value
            if num % x != target_mod:
                return -1
            
            # The number of operations is the absolute distance divided by the step size 'x'
            total_operations += abs(num - median) // x
            
        return total_operations

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard valid grid
    print(f"Test 1: {sol.minOperations([[2,4],[6,8]], 2)}") 
    # Expected: 4 
    # (Flattened: [2, 4, 6, 8]. Median is 6. 
    # 2 needs 2 steps. 4 needs 1 step. 8 needs 1 step. 2+1+1 = 4 operations)
    
    # Test 2: Impossible grid
    print(f"Test 2: {sol.minOperations([[1,5],[2,3]], 1)}") 
    # Expected: 5 (Median is 2. Modulo matches for x=1. Steps: 1+3+0+1 = 5)
    
    # Test 3: Modulo mismatch trap
    print(f"Test 3: {sol.minOperations([[1,2],[3,4]], 2)}") 
    # Expected: -1 (1 % 2 = 1, but 2 % 2 = 0. They can never meet by adding/subtracting 2)s