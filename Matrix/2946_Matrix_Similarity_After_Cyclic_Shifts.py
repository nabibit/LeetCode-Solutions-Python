# Problem: 2946. Matrix Similarity After Cyclic Shifts
# Difficulty: Easy
# Link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description

# Time Complexity: O(M * N) - We check every row of length N exactly once.
# Space Complexity: O(N) - Python creates a temporary list of size N during the slice concatenation.

from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])

        # Shifting by the length of the row does nothing
        # So we only need to shift by the remainder
        k = k % n

        # If the effective shift is 0, the matrix obviously remains identical
        if k ==0:
            return True

        for i in range(len(mat)):
            row = mat[i]
            if i % 2 == 0:
                # Even Row: Left Shift
                # The first 'k' elements move to the very back
                shifted_row = row[k:] + row[:k]
            else:
                # Odd Row: Right Shift
                # The last 'k' elements move to the very front
                shifted_row = row[-k:] + row[:-k]

            # If our virtually shifted row doesn't match the original, we fail
            if shifted_row != row:
                return False

        return True
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Symmetric shifts that perfectly align
    print(f"Test 1: {sol.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2)}") 
    # Expected: True 
    
    # Test 2: Shifts that break the pattern
    print(f"Test 2: {sol.areSimilar([[2,2],[1,2],[3,4]], 1)}") 
    # Expected: False