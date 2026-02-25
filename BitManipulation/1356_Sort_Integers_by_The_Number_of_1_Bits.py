# Problem: 1356. Sort Integers by The Number of 1 Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description

# Time Complexity: O(N log N) - We sort the array in place after our bitwise operation
# Space Complexity: O(1) extra space - We modify the integers in place, avoiding any tuple or object allocation overhead

from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # We merge the bit count and the original value into a single integer
        # Since the max value is 10000 (which fits in 14 bits), we shift the count left by 14
        for i in range(len(arr)):
            arr[i] += (arr[i].bit_count() << 14)

        # We perform an in-place sort on the pure integers, bypassing tuple onject creation entirely
        arr.sort()

        # We apply a bitmask to strip away the upper bits, restoring the original numbers
        # 16383 is exactly (1 << 14) -1, which represent 14 binary ones
        for i in range(len(arr)):
            arr[i] &= 16383

        return arr
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: Standard mix of integers
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Expected: [0, 1, 2, 4, 8, 3, 5, 6, 7]
    print(f"Test 1: {solution.sortByBits(arr1)}")
    
    # Test 2: Identical bit counts, sorted by value
    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    # Expected: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    print(f"Test 2: {solution.sortByBits(arr2)}")