# Problem: 1727. Largest Submatrix With Rearrangements
# Difficulty: Medium
# Link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/description

# Time Complexity: O(M * N log N) - We iterate through the matrix and sort each row of length N
# Space Complexity: O(1) - We modify the grid in-place to store the histogram heights

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                # Step 1: Calculate consecutive column heights
                # If the cell is 1 and it's not the top row, add the height of the 1s stacked above it
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
                    
            # Step 2: Sort the current row's heights in descending order
            # We copy the row to sort so we don't mess up the original vertical column alignments
            # for the subsequent rows we still need to process
            sorted_heights = sorted(matrix[i], reverse=True)
            
            # Step 3: Calculate the maximum possible rectangle for this row
            for k in range(cols):
                # The width is (k + 1) because it's 0-indexed
                # The height is limited by the current column in our sorted list
                current_area = sorted_heights[k] * (k + 1)
                max_area = max(max_area, current_area)
                
        return max_area

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple 3x3 matrix
    matrix1 = [[0,0,1],[1,1,1],[1,0,1]]
    print(f"Test 1: {sol.largestSubmatrix(matrix1)}") # Expected: 4
    
    # Test 2: Single row
    matrix2 = [[1,0,1,0,1]]
    print(f"Test 2: {sol.largestSubmatrix(matrix2)}") # Expected: 3