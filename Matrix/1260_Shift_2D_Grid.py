# Problem: 1260. Shift 2D Grid
# Difficulty: Easy
# Link: https://leetcode.com/problems/shift-2d-grid/description

# Time Complexity: O(M * N) - We visit each cell in the M x N grid exactly once to build the answer.
# Space Complexity: O(M * N) - We allocate a new 2D array of the exact same size to store the shifted result.

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_cells = m * n
        
        # If we shift the grid by its total size, it wraps around to its original state.
        # We only need the remainder.
        k = k % total_cells
        
        # If k is 0 after modulo, no shifts are needed
        if k == 0:
            return grid
            
        ans = []
        for r in range(m):
            new_row = []
            for c in range(n):
                # Calculate what the 1D index of this specific cell is
                curr_1d_index = r * n + c
                
                # To find out what number belongs here, we run the clock backwards by 'k'
                # The modulo operator beautifully handles all the matrix wrap-arounds instantly
                orig_1d_index = (curr_1d_index - k) % total_cells
                
                # Convert that 1D index back into its original 2D row and column
                orig_r = orig_1d_index // n
                orig_c = orig_1d_index % n
                
                # Grab the exact number and drop it into our new row
                new_row.append(grid[orig_r][orig_c])
                
            ans.append(new_row)
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard shift
    print(f"Test 1: {sol.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1)}") 
    # Expected: [[9,1,2],[3,4,5],[6,7,8]]
    
    # Test 2: Shift wraps around multiple times
    print(f"Test 2: {sol.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4)}") 
    # Expected: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    
    # Test 3: Shift matches the grid size (returns original)
    print(f"Test 3: {sol.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9)}") 
    # Expected: [[1,2,3],[4,5,6],[7,8,9]]