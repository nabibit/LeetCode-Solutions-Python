# Problem: 1886. Determine Whether Matrix Can Be Obtained By Rotation
# Difficulty: Easy
# Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description

# Time Complexity: O(N^2) - We rotate a maximum of 4 times. Each rotation visits every element.
# Space Complexity: O(1) - We rotate the matrix perfectly in-place using transpositions and reversals.

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        # We check all 4 possible orientations: 0, 90, 180, and 270 degrees
        for _ in range(4):
            # Check if our current rotation matches the target
            if mat == target:
                return True

            # Perform a 90-degreee clockwise rotation in-place:

            # Transpose the matrix (swap mat[i][j] with mat[j][i])
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # Reverse each row horizontally
            for i in range(n):
                mat[i].reverse()

        # If we spun it 360 degrees and never found a match, it's impossible
        return False
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 90 degree rotation
    mat1 = [[0,1],[1,0]]
    target1 = [[1,0],[0,1]]
    print(f"Test 1: {sol.findRotation(mat1, target1)}") # Expected: True
    
    # Test 2: Impossible rotation
    mat2 = [[0,1],[1,1]]
    target2 = [[1,0],[0,1]]
    print(f"Test 2: {sol.findRotation(mat2, target2)}") # Expected: False
    
    # Test 3: Multiple rotations needed
    mat3 = [[0,0,0],[0,1,0],[1,1,1]]
    target3 = [[1,1,1],[0,1,0],[0,0,0]]
    print(f"Test 3: {sol.findRotation(mat3, target3)}") # Expected: True