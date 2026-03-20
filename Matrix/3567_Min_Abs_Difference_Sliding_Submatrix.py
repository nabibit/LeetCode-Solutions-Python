# Problem: 3567. Minimum Absolute Difference in Sliding Submatrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description

# Time Complexity: O(M - K + 1) * (N - K + 1) * K^2 log(K)) - We iterate through every top-left corner, extract K^2 elements, and sort them. Given the tiny constraints (M, N <= 30), this runs phenomenally fast.
# Space Complexity: O(K^2) - We create a temporary array of size K^2 to sort the extracted submatrix elements.

from typing import List 

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])

        # Initialize our result matrix with zeros
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Extract and flatten the k x k submatrix into a 1D, then sort it
                nums = sorted(grid[x][y] for x in range(i, i + k) for y in range(j, j + k))

                min_diff = float('inf')

                # Check adjacent elements in the sorted list to find the minimum gap
                for t in range(1, len(nums)):
                    if nums[t] != nums[t - 1]: # The problem strictly requires distinct values
                        min_diff = min(min_diff, nums[t] - nums[t - 1])

                # If we never found a valid difference (e.g., all numbers are identical), return 0
                ans[i][j] = min_diff if min_diff != float('inf') else 0
        return ans
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: k = 2
    grid1 = [[1, -2, 3], [2, 3, 5]]
    print(f"Test 1: {sol.minAbsDiff(grid1, 2)}") 
    # Expected: [[1, 2]]
    
    # Test 2: Identical elements (k = 1)
    grid2 = [[3, -1]]
    print(f"Test 2: {sol.minAbsDiff(grid2, 1)}") 
    # Expected: [[0, 0]]