# Problem: 2144. Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description

# Time Complexity: O(N log N) - We sort the array of candies in descending order. The linear scan tale O(N) time.
# Space Complexity: O(1) - Constant auxiliary space (ignoring the memory used by Python's built-in sorting algorithm).

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        total_cost = 0

        for i in range(len(cost)):
            if i % 3 != 2:
                total_cost += cost[i]

        return total_cost
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard discount
    print(f"Test 1: {sol.minimumCost([1, 2, 3, 4])}") 
    # Expected: 8
    # (Sorted: [4, 3, 2, 1]. Buy 4 and 3, get 2 free. Buy 1. Total: 4 + 3 + 1 = 8)
    
    # Test 2: Multiple free candies
    print(f"Test 2: {sol.minimumCost([6, 5, 7, 9, 2, 2])}") 
    # Expected: 23
    # (Sorted: [9, 7, 6, 5, 2, 2]. Buy 9 and 7, get 6 free. Buy 5 and 2, get 2 free. Total: 9 + 7 + 5 + 2 = 23)
    
    # Test 3: Not enough for a discount
    print(f"Test 3: {sol.minimumCost([5, 5])}") 
    # Expected: 10
    # (Sorted: [5, 5]. Buy 5 and 5, none free. Total: 10)