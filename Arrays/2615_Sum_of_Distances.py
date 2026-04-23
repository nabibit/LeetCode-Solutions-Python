# Problem: 2615. Sum of Distances
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-of-distances/description

# Time Complexity: O(N) - We iterate through the aray to build the hash map, and then iterate through the grouped indices exactly once.
# Space Complexity: O(N) - We store though the grouped indices and allocate an answer array.

from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Map each unique number to a list of its indices
        pos_map = defaultdict(list)
        for i, num in enumerate(nums):
            pos_map[num].append(i)

        ans = [0] * len(nums)

        # Process each group of identical numbers
        for indices in pos_map.values():
            # Initial state: we assume we are standing at the very first index
            # EVERYTHING is to our right, and NOTHING is to our left
            right_sum = sum(indices)
            left_sum = 0

            right_count = len(indices)
            left_count = 0

            for i in indices:
                # Remove the current index from the right "pool" (we are standing on it now)
                right_sum -= i
                right_count -= 1

                # Calculate the total distance to all positions on the left
                # Math: (How many positions on left * my position) - (sum of their actual positions)
                left_distance = (left_count * i) - left_sum
                
                # Calculate the total distance to all friends on the right
                # Math: (sum of their actual positions) - (How many positions on right * my position)
                right_distance = right_sum - (right_count * i)

                # Save the total combined distance
                ans[i] = left_distance + right_distance

                # Add our current position to the "left" pool before we step forward to the next index
                left_sum += i
                left_count += 1
        
        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple occurrences
    print(f"Test 1: {sol.distance([1, 3, 1, 1, 2])}") 
    # Expected: [5, 0, 3, 4, 0]
    # Explanation for '1' at indices [0, 2, 3]:
    # Index 0: |0-2| + |0-3| = 5
    # Index 2: |2-0| + |2-3| = 3
    # Index 3: |3-0| + |3-2| = 4
    
    # Test 2: Only unique numbers
    print(f"Test 2: {sol.distance([2, 0, 2, 2, 6, 5, 2])}") 
    # Expected: [11, 0, 7, 7, 0, 0, 13]