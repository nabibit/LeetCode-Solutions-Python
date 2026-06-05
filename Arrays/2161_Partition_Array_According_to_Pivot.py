# Problem: 2161. Partition Array According to Given Pivot
# Difficulty: Medium
# Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/description

# Time Complexity: O(N) - We iterate through the array exactly once. Array concatenation takes O(N).
# Space Complexity: O(N) - We create three temporary arrays that collectively store N elements.

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        
        # Sweep the array and drop elements into their respective buckets
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
                
        # Concatenate the buckets. This perfectly preserves the original relative order!
        return less + equal + greater

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Partition
    print(f"Test 1: {sol.pivotArray([9, 12, 5, 10, 14, 3, 10], 10)}") 
    # Expected: [9, 5, 3, 10, 10, 12, 14]
    
    # Test 2: Negative numbers and multiple pivots
    print(f"Test 2: {sol.pivotArray([-3, 4, 3, 2], 2)}") 
    # Expected: [-3, 2, 4, 3]