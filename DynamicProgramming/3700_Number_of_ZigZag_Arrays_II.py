# Problem: 3700. Number of ZigZag Arrays II
# Difficulty: Hard
# Link: https://leetcode.com/problems/number-of-zigzag-arrays-ii/description

# Time Complexity: O(M^3 log N) - Where M is the range size (r - l + 1). We perform M x M matrix multiplications O(log N) times. Since M <= 100, M^3 is tiny, making N = 10^9 execute instantly.
# Space Complexity: O(M^2) - We store M x M transition grids in auxiliary memory.

from typing import List

class Solution:
    def numberOfZigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1  # The count of available numbers in our range [l, r]
        
        # If length is 1, any single number from our range is valid
        if n == 1:
            return m % MOD
            
        # If length is 2, any pair of DIFFERENT numbers is valid
        # There are m choices for the first number, and m - 1 choices for the second
        if n == 2:
            return (m * (m - 1)) % MOD
            
        # PURE PYTHON MATRIX MATH HELPERS
        
        # Helper 1: Multiplies two M x M matrices (mat1 * mat2)
        def multiply_matrices(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
            # zip(*mat2) flips the columns of mat2 into rows so Python can easily loop over them
            mat2_columns = list(zip(*mat2))
            
            result = []
            for row in mat1:
                new_row = []
                for col in mat2_columns:
                    # Dot product: sum up (row_cell * col_cell) across the row and column
                    cell_sum = sum(a * b for a, b in zip(row, col)) % MOD
                    new_row.append(cell_sum)
                result.append(new_row)
            return result
            
        # Helper 2: Raises a matrix to a massive power (matrix^exp) in O(log exp) time
        def power_matrix(base_matrix: List[List[int]], exp: int) -> List[List[int]]:
            # Initialize result as the Identity Matrix (the matrix equivalent of the number '1')
            # The main diagonal is all 1s, everything else is 0s.
            result = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
            
            current_base = base_matrix
            while exp > 0:
                # If the current exponent is odd, multiply our result by the base
                if exp % 2 == 1:
                    result = multiply_matrices(result, current_base)
                # Square the base matrix and cut the exponent in half (Binary Exponentiation)
                current_base = multiply_matrices(current_base, current_base)
                exp //= 2
            return result
            
        # Helper 3: Multiplies an M x M matrix by a 1D vector of size M
        def multiply_matrix_vector(mat: List[List[int]], vec: List[int]) -> List[int]:
            return [sum(cell * val for cell, val in zip(row, vec)) % MOD for row in mat]

        # ZIGZAG TRANSITION ENGINE
        
        # Matrix A defines valid UP steps (stepping from previous number 'prev' -> current number 'curr')
        # A[curr][prev] = 1 if curr > prev (meaning we successfully stepped UP)
        A = [[1 if curr > prev else 0 for prev in range(m)] for curr in range(m)]
        
        # Matrix B defines valid DOWN steps (stepping from previous number 'prev' -> current number 'curr')
        # B[curr][prev] = 1 if curr < prev (meaning we successfully stepped DOWN)
        B = [[1 if curr < prev else 0 for prev in range(m)] for curr in range(m)]
        
        # Initial state vectors at Length 2
        # up2[v]: count of length-2 arrays ending at value 'v' that went UP (v choices below it)
        # down2[v]: count of length-2 arrays ending at value 'v' that went DOWN (m - 1 - v choices above it)
        up2 = [v for v in range(m)]
        down2 = [m - 1 - v for v in range(m)]
        
        # Every combined pair of steps (A * B) or (B * A) moves our array forward by 2 length
        # We start at length 2, so we have (n - 2) steps remaining to reach length n
        steps_remaining = n - 2
        double_steps = steps_remaining // 2
        
        # Precompute (A * B)^double_steps and (B * A)^double_steps instantly
        AB_powered = power_matrix(multiply_matrices(A, B), double_steps)
        BA_powered = power_matrix(multiply_matrices(B, A), double_steps)
        
        # If remaining steps is EVEN, we just apply our powered double-step engines directly
        if steps_remaining % 2 == 0:
            # (A * B) applies a DOWN step then an UP step. Applied to up2, it creates up_n
            final_up = multiply_matrix_vector(AB_powered, up2)
            # (B * A) applies an UP step then a DOWN step. Applied to down2, it creates down_n
            final_down = multiply_matrix_vector(BA_powered, down2)
        else:
            # If remaining steps is ODD, we apply the double-steps PLUS one final alternating step
            # An UP ending comes from applying Matrix A to the final DOWN states.
            final_up = multiply_matrix_vector(A, multiply_matrix_vector(BA_powered, down2))
            # A DOWN ending comes from applying Matrix B to the final UP states.
            final_down = multiply_matrix_vector(B, multiply_matrix_vector(AB_powered, up2))
            
        # The total number of valid ZigZag arrays is the sum of all valid final states
        return (sum(final_up) + sum(final_down)) % MOD

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Small range (n=3, range [4,5]) -> Expected: 2 ([4,5,4], [5,4,5])
    print(f"Test 1: {sol.numberOfZigZagArrays(3, 4, 5)}") 
    
    # Test 2: Standard check (n=4, range [1,5]) -> Expected: 170
    print(f"Test 2: {sol.numberOfZigZagArrays(4, 1, 5)}") 
    
    # Test 3: The 1-Billion Constraint Check!
    print(f"Test 3: {sol.numberOfZigZagArrays(10**9, 1, 5)}")