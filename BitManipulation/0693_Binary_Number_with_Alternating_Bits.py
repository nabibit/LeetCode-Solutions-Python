# Problem: 693. Binary Number with Alternating Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-number-with-alternating-bits/description

# Time Complexity: O(1) - Constant number of bitwise operations. No loops
# Space Complexity: O(1) - Uses almost no memory

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # We shift n to the right by 1 and XOR it with the original n
        # If n is alternating (e.g., 101), then n>>1 is 010.
        # 101 ^ 010 = 111 (All bits become 1)
        a = n ^ (n >> 1)

        # We verify that 'a' consists ONLY of 1s(e.g., 111, 11111)
        # If 'a' is all 1s, then 'a + 1' will be power of 2 (1.g., 1000)
        # A number 'a' ANDed with 'a + 1' should be 0 if 'a' is all 1s
        return (a & (a + 1)) == 0
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: 5 (101) -> True
    print(solution.hasAlternatingBits(5))
    
    # Test Case 2: 7 (111) -> False
    # 7 ^ 3 = 111 ^ 011 = 100. (4 & 5) != 0.
    print(solution.hasAlternatingBits(7))
    
    # Test Case 3: 11 (1011) -> False
    print(solution.hasAlternatingBits(11))