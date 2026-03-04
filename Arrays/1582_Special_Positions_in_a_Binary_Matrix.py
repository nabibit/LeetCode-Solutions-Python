# Problem: 1582. Special Positions in a Binary Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/description

# Time Complexity: O(M * N) - We scan the matrix to calculate sums, then scan it again to check positions
# Space Complexity: O(M + N) - We store the sum of each row and each column in two separate arrays

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        # We precalculate the total sum of elements for each row
        row_sums = [sum(row) for row in mat]

        # We precalculate the total sum of elements for each column
        col_sums = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]
        
        special_count = 0

        # We iterate throguh every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # A position is special if it is a '1' AND it is ONLY '1' in its row and column
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1

        return special_count
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Two special positions
    mat1 = [[1,0,0],[0,0,1],[1,0,0]]
    print(f"Test 1: {sol.numSpecial(mat1)}") # Expected: 1
    
    # Test 2: One special position
    mat2 = [[1,0,0],[0,1,0],[0,0,1]]
    print(f"Test 2: {sol.numSpecial(mat2)}") # Expected: 3