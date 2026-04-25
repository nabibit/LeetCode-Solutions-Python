# Problem: 3464. Maximize the Distance Between Points on a Square
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/description

# Time Complexity: O(N log N + log(side) * N * k) - Sorting takes O(N log N). Our binary search range is log(10^9) ~ 30 iterations. Inside, the check does an O(N) precomputation and an O(N * k) sweep. Highly optimal.
# Space Complexity: O(N) - We store the flattened 1D array of points.

from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 1. Unroll the 2D square boundary into a 1D line of length 4 * side
        mapped = []
        for x, y in points:
            if y == 0:
                mapped.append(x)                    # Bottom edge
            elif x == side:
                mapped.append(side + y)             # Right edge
            elif y == side:
                mapped.append(3 * side - x)         # Top edge
            else:
                mapped.append(4 * side - y)         # Left edge
                
        mapped.sort()
        
        # 2. Duplicate the array to easily handle circular wrap-around math
        arr2 = mapped + [v + 4 * side for v in mapped]
        N = len(mapped)
        N2 = len(arr2)
        limit_dist = 4 * side
        
        # 3. Helper function to test if a candidate distance 'm' is mathematically possible
        def check(m: int) -> bool:
            # Precompute the "next valid jump" index for every point using a sliding window
            next_idx = [N2] * N2
            j = 0
            for i in range(N2):
                while j < N2 and arr2[j] - arr2[i] < m:
                    j += 1
                next_idx[i] = j
                
            # The maximum allowed distance span to ensure the wrap-around gap is ALSO >= m
            max_allowed_span = limit_dist - m
            
            # Try starting our sequence from each of the original N points
            for i in range(N):
                curr = i
                
                # Make k - 1 greedy jumps to place all remaining points
                for _ in range(k - 1):
                    curr = next_idx[curr]
                    if curr >= N2:
                        break
                
                # If we placed all k points AND the total perimeter distance spanned leaves 
                # enough room for the final wrap-around jump back to the start
                if curr < N2 and arr2[curr] - arr2[i] <= max_allowed_span:
                    return True
                    
            return False

        # 4. Binary Search on Answer
        # The answer must be at least 1, and can never exceed `side` (since k >= 4)
        low, high = 1, side
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1  # This distance works, try to stretch it even bigger!
            else:
                high = mid - 1 # Distance is too big, it failed. Shrink it.
                
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Select all 4 corners
    print(f"Test 1: {sol.maxDistance(2, [[0,2],[2,0],[2,2],[0,0]], 4)}") 
    # Expected: 2 (Distance between any two adjacent corners is exactly 'side' which is 2)
    
    # Test 2: Select an offset group of 4
    print(f"Test 2: {sol.maxDistance(2, [[0,0],[1,2],[2,0],[2,2],[2,1]], 4)}") 
    # Expected: 1