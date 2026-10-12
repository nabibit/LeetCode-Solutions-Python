# Problem: 2897. Apply Operations on Array to Maximize Sum of Squares
# Difficulty: Hard
# Link: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

# Time Complexity: O(N) - We iterate through the array of length N once, evaluating 32 bits per number. Constructing the K numbers also takes O(K * 32). This simplifies to strict O(N) linear time.
# Space Complexity: O(1) - We allocate a fixed integer array of size 32 to track bit frequencies, completely independent of the input size.

from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Count the total frequency of each bit across the entire array
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_counts[i] += 1
                    
        ans = 0
        
        # Step 2: Greedily construct the K largest possible numbers
        for _ in range(k):
            current_num = 0
            for i in range(32):
                # If we have this bit available, attach it to our current number
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
                    
            # Add the squared value to the total and apply the modulo
            ans = (ans + current_num * current_num) % MOD
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard bit concentration
    print(f"Test 1: {sol.maxSum([2,6,5,8], 2)}") 
    # Expected: 261
    
    # Test 2: Take all elements (operations don't change the total bits)
    print(f"Test 2: {sol.maxSum([4,5,4,7], 3)}") 
    # Expected: 90