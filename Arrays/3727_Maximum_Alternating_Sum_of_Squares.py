# Problem: 3727. Maximum Alternating Sum of Squares
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-alternating-sum-of-squares/

# Time Complexity: O(N log N) - We sort the array based on absolute values. The subsequent sweep takes O(N) linear time.
# Space Complexity: O(1) - The sorting operates in-place, and we only use a single accumulator variable.

from typing import List

class Solution:
    def maximumAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Sort ascending by absolute value 
        # so the weakest numbers are at the front of the array
        nums.sort(key=abs)
        
        n = len(nums)
        # In any array, exactly floor(N / 2) elements will sit on odd (subtractive) indices
        num_negatives = n // 2
        
        ans = 0
        
        # Step 2: Subtract the squares of the smallest absolute values
        for i in range(num_negatives):
            ans -= nums[i] * nums[i]
            
        # Step 3: Add the squares of all the remaining (largest) absolute values
        for i in range(num_negatives, n):
            ans += nums[i] * nums[i]
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Partitioning beats interleaving
    print(f"Test 1: {sol.maximumAlternatingSum([1, 2, 3])}") 
    # Expected: 12 
    # (Sorted by abs: [1, 2, 3]. N=3, so 1 negative spot. 
    # Smallest is 1 -> -1^2. Remaining are 2,3 -> +2^2 +3^2. Total = 12)
    
    # Test 2: Even length array
    print(f"Test 2: {sol.maximumAlternatingSum([1, 2, 3, 4])}") 
    # Expected: 20
    # (Sorted by abs: [1, 2, 3, 4]. N=4, so 2 negative spots.
    # Smallest two are 1,2 -> -1^2 - 2^2. Remaining are 3,4 -> +3^2 + 4^2. Total = 20)