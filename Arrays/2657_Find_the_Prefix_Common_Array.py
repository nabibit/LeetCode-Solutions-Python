# Problem: 2657. Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description

# Time Complexity: O(N) - We iterate tjrough the arrays exactly once. Array lookups and updates are O(1).
# Space Complexity: O(N) - We use a frquency array of size N + 1 to track seen elements, plus the output array.

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        # A frquency array to track how many times we've seen each number (1 to n)
        seen_counts = [0] * (n + 1)

        prefix_common = []
        common_count = 0

        for i in range(n):
            # Process the number from array A
            seen_counts[A[i]] += 1
            # If the count reaches 2, it means it has appeared in both A and B
            if seen_counts[A[i]] == 2:
                common_count += 1 

            # Process the number from array B
            seen_counts[B[i]] += 1
            # If the count reaches 2, it means it has appeared in both A and B
            if seen_counts[B[i]] == 2:
                common_count += 1

            # Append the current running total to our result
            prefix_common.append(common_count)

        
        return prefix_common
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Permutations
    print(f"Test 1: {sol.findThePrefixCommonArray([1,3,2,4], [3,1,2,4])}") 
    # Expected: [0, 2, 3, 4]
    
    # Test 2: Identical Permutations
    print(f"Test 2: {sol.findThePrefixCommonArray([2,3,1], [3,1,2])}") 
    # Expected: [0, 1, 3]