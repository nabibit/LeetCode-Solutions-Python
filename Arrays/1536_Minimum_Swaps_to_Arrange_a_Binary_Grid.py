# Problem: 1536. Minimum Swaps to Arrange a Binary Grid
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/

# Time Complexity: O(N^2) - We iterate throguh the grid to count trailing zeros, and in the worst case, shofting elements takes O(N^2)
# Space Complexity: O(N) - We store the count of trailing zeros for each row in a list of size N

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # We use a quick list comprehension with a next() generator to find the trailing zeros
        tz = [next((c for c, val in enumerate(reversed(row)) if val == 1), n) for row in grid]

        ans = 0
        for i in range(n):
            target = n - 1 - i

            # We find the index of the first row that meets the target
            j = i
            while j < n and tz[j] < target:
                j += 1
            
            if j == n:
                return -1

            # We add the number of swaps needed and stimulate the shift using pop and insert
            ans += (j - i)
            tz.insert(i, tz.pop(j))

        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Grid can be fixed in 3 swaps
    grid1 = [[0,0,1],[1,1,0],[1,0,0]]
    print(f"Test 1: {sol.minSwaps(grid1)}") # Expected: 3
    
    # Test 2: Grid is already valid
    grid2 = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
    print(f"Test 2: {sol.minSwaps(grid2)}") # Expected: -1 (Impossible)
    
    # Test 3: Grid is already perfect
    grid3 = [[1,0,0],[0,1,0],[0,0,1]]
    print(f"Test 3: {sol.minSwaps(grid3)}") # Expected: 0