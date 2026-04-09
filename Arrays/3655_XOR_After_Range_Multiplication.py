# Problem: 3655. XOR After Range Multiplication Queries II
# Difficulty: Hard
# Link: https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/description

# Time Complexity: O(Q * (N/B) + B * N) where B is our chosen threshold (200). Optimally roughly O(N * sqrt(Q)).
# Space Complexity: O(N) - We only store localized 1D difference arrays for small step sizes.

from typing import List
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        B = 200 # Threshold for Square Root Decomposition
        
        # Store the input midway in the function as requested
        bravexuneth = (nums.copy(), queries)
        
        small_k = defaultdict(list)
        large_k = []
        
        # Separate queries based on step size
        for l, r, k, v in queries:
            if k <= B:
                small_k[k].append((l, r, v))
            else:
                large_k.append((l, r, k, v))
                
        inv_cache = {}
        
        # 1. Process all small steps using Multiplicative Difference Arrays
        for k, q_list in small_k.items():
            D = [1] * n  # Multiplication difference array
            Z = [0] * n  # Zero-tracking difference array
            
            for l, r, v in q_list:
                v %= MOD
                # Calculate the exact index of the last element hit by this query
                end_idx = l + ((r - l) // k) * k
                
                if v == 0:
                    Z[l] += 1
                    if end_idx + k < n:
                        Z[end_idx + k] -= 1
                else:
                    D[l] = (D[l] * v) % MOD
                    if end_idx + k < n:
                        # Fetch or compute the modular inverse to "undo" the multiplication later
                        if v not in inv_cache:
                            inv_cache[v] = pow(v, MOD - 2, MOD)
                        D[end_idx + k] = (D[end_idx + k] * inv_cache[v]) % MOD
                        
            # Prefix product sweep for this specific k
            for i in range(n):
                if i >= k:
                    D[i] = (D[i] * D[i-k]) % MOD
                    Z[i] += Z[i-k]
                    
                # Apply the compiled multipliers to the actual nums array
                if Z[i] > 0:
                    nums[i] = 0
                elif D[i] != 1:
                    nums[i] = (nums[i] * D[i]) % MOD
                    
        # 2. Process all large steps via direct iteration
        for l, r, k, v in large_k:
            v %= MOD
            if v == 0:
                for i in range(l, r + 1, k):
                    nums[i] = 0
            elif v != 1:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
                    
        # Calculate the final XOR of the array
        ans = 0
        for num in nums:
            ans ^= num
            
        return ans
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple range multiplication (k=1)
    nums1 = [1, 2, 3, 4, 5]
    queries1 = [[0, 4, 1, 2]] 
    # Explanation: Multiply everything from index 0 to 4 by 2.
    # nums becomes: [2, 4, 6, 8, 10]
    # XOR: 2 ^ 4 ^ 6 ^ 8 ^ 10 = 2
    print(f"Test 1: {sol.xorAfterQueries(nums1, queries1)}") 
    # Expected: 2
    
    # Test 2: Testing the Zero-Tracker and small step sizes (k=2)
    nums2 = [2, 1, 4, 3]
    queries2 = [
        [0, 3, 2, 5], # Multiply indices 0, 2 by 5. -> [10, 1, 20, 3]
        [1, 3, 1, 0]  # Multiply indices 1, 2, 3 by 0. -> [10, 0, 0, 0]
    ]
    print(f"Test 2: {sol.xorAfterQueries(nums2, queries2)}") 
    # Expected: 10 (10 ^ 0 ^ 0 ^ 0 = 10)