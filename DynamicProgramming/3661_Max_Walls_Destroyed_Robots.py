# Problem: 3661. Maximum Walls Destroyed by Robots
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-walls-destroyed-by-robots/description

# Time Complexity: O(R log R + W log W) - Sorting the robots and walls takes O(R log R) and O(W log W). The DP iteration performs binary searches taking O(R log W).
# Space Complexity: O(R + W) - We store the sorted arrays and the O(R) DP state arrays (only_L, only_R, shared).

from typing import List
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        
        #  Sort robots by position, keeping their original distances attached
        bots = sorted(zip(robots, distance))
        walls_sorted = sorted(walls)

        pos  = [b[0] for b in bots]
        dist = [b[1] for b in bots]

        # Helper to count walls in an inclusive range [lo, hi]
        def count_walls(lo: int, hi: int) -> int:
            if lo > hi:
                return 0
            return bisect.bisect_right(walls_sorted, hi) - bisect.bisect_left(walls_sorted, lo)

        #  Precompute the isolated gap zones for every pair of adjacent robots
        # only_L[i] = Walls in gap 'i' reachable ONLY by Robot 'i' (shooting Right)
        # only_R[i] = Walls in gap 'i' reachable ONLY by Robot 'i+1' (shooting Left)
        # shared[i] = Walls in gap 'i' reachable by BOTH robots
        only_L = [0] * (n - 1)
        only_R = [0] * (n - 1)
        shared = [0] * (n - 1)

        for i in range(n - 1):
            gap_start   = pos[i] + 1
            gap_end     = pos[i + 1] - 1
            
            if gap_start > gap_end:
                continue

            right_reach = min(pos[i] + dist[i],         gap_end)
            left_reach  = max(pos[i + 1] - dist[i + 1], gap_start)

            if left_reach <= right_reach:
                # The beams overlap! Isolate the shared middle section
                shared[i] = count_walls(left_reach, right_reach)
                only_L[i] = count_walls(gap_start,      left_reach - 1)
                only_R[i] = count_walls(right_reach + 1, gap_end)
            else:
                # The beams fall short of each other. No shared section.
                shared[i] = 0
                only_L[i] = count_walls(gap_start,  right_reach)
                only_R[i] = count_walls(left_reach,  gap_end)

        # Walls exactly ON the robot's position are unconditionally destroyed
        at_pos = [count_walls(pos[i], pos[i]) for i in range(n)]

        # Handle the infinite void ranges for the first and last robots
        solo_left_0  = count_walls(pos[0] - dist[0],         pos[0] - 1)
        solo_right_n = count_walls(pos[n-1] + 1, pos[n-1] + dist[n-1])

        # Edge Case: Only 1 robot exists
        if n == 1:
            return max(solo_left_0, solo_right_n) + at_pos[0]

        # DP Initialization for the first robot
        dp_L = solo_left_0           + at_pos[0]   # Robot 0 fires Left into the void
        dp_R = only_L[0] + shared[0] + at_pos[0]   # Robot 0 fires Right into Gap 0

        # DP Transitions
        for i in range(1, n):
            prev_L, prev_R = dp_L, dp_R

            # If Prev fired Right, Prev already claimed the 'shared' zone. We only get 'only_R'.
            gain_L_from_R = only_R[i - 1]                   
            # If Prev fired Left, Prev ignored the gap entirely! We get BOTH 'only_R' and 'shared'.
            gain_L_from_L = only_R[i - 1] + shared[i - 1]   

            new_L = max(prev_R + gain_L_from_R, 
                        prev_L + gain_L_from_L) + at_pos[i]

            # Firing right has no conflict with the previous robot, so we just take the max history 
            # and claim our 'only_L' and 'shared' properties for the NEW gap ahead of us.
            if i < n - 1:
                gain_R = only_L[i] + shared[i]
                new_R  = max(prev_L, prev_R) + gain_R + at_pos[i]
            else:
                # The final robot shoots right into the infinite void
                new_R  = max(prev_L, prev_R) + solo_right_n + at_pos[i]

            dp_L, dp_R = new_L, new_R

        return max(dp_L, dp_R)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: The previously failing overlap trap (Case 3)
    print(f"Test 1: {sol.maxWalls([10, 2], [5, 1], [5, 2, 7])}") 
    # Expected: 3 
    
    # Test 2: Basic separation
    print(f"Test 2: {sol.maxWalls([1, 5], [2, 3], [0, 2, 4, 6])}") 
    # Expected: 3