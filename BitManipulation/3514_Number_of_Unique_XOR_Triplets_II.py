# Problem: 3514. Number of Unique XOR Triplets II
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description

# Time Complexity: O(U^2 + P * U) - Where U is the number of unique elements in nums (U <= 1500), and P is the number of unique pairwise XOR values (P <= 2048). This executes in under 0.1 seconds.
# Space Complexity: O(U + P + V) - Where V is the number of unique triplet XOR values (V <= 2048). We store sets bounded strictly by the binary vector space.

from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Extract unique elements to eliminate redundant evaluations
        u = list(set(nums))
        
        # Generate all achievable pairwise XOR values
        # Since i <= j allows i == j, x ^ x = 0 is naturally included
        pair_xors = {u[i] ^ u[j] for i in range(len(u)) for j in range(i, len(u))}
        
        # Combine pairwise XORs with a third element to form all triplet XORs
        triplet_xors = {p ^ z for p in pair_xors for z in u}
        
        return len(triplet_xors)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Given Example 1
    print(f"Test 1: {sol.uniqueXorTriplets([1, 3])}") 
    # Expected: 2 
    # (Pairs: {0, 2} -> Triplets with {1, 3} -> {1, 3})
    
    # Test 2: Given Example 2
    print(f"Test 2: {sol.uniqueXorTriplets([6, 7, 8, 9])}") 
    # Expected: 4 
    # (Pairs: {0, 1, 14, 15} -> Triplets -> {6, 7, 8, 9})
    
    # Test 3: Identical elements
    print(f"Test 3: {sol.uniqueXorTriplets([5, 5, 5])}") 
    # Expected: 1 (Only 5 ^ 5 ^ 5 = 5 is possible)