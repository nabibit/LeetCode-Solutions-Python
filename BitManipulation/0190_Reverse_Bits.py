# Problem: 190. Reverse Bits
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-bits/description/

# Time Complexity: O(1) - Executes exactly 5 bitwise merge operations. No loops
# Space Complexity: O(1) - Strictly constant space.  No arrays or cache overhead

class Solution:
    def reverseBits(self, n: int) -> int:
        # We use a Divide and Conquer approach to swap bits in parallel
        # This is preferred over a Lookup Tbale because ALU opreations (1 cycle)
        # are typically faster than L1 Cache loads (3-4 cycles), and we avoid
        # cache pollution

        # Step 1: Swap adjacent bits
        # Mask 0x55555555 is ...01010101. We select odd bits, shift right,
        # select even bits, shift left, then merge
        n = (n >> 1) & 0x55555555 | ((n & 0x55555555) << 1)

        # Step 2: Swap 2-bit pairs
        # Mask 0x33333333 is ...00110011
        n = (n >> 2) & 0x33333333 | ((n & 0x33333333) << 2)

        # Step 3: Swap 4-bit nibbles
        # Mask 0x0F0F0F0F is ...00001111
        n = (n >> 4) & 0x0F0F0F0F | ((n & 0x0F0F0F0F) << 4)

        # Step 2: Swap bytes(8 bits)
        # Mask 0x00FF00FF is ...0000000011111111
        n = (n >> 8) & 0x00FF00FF | ((n & 0x00FF00FF) << 8)

        # Step 5: Swap 16-bit halves
        # Mask 0x0000FFFF is the lower 16 bits
        n = (n >> 16) & 0x0000FFFF | ((n & 0x0000FFFF) << 16)

        return n
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test: 43261596 (00000010100101000001111010011100)
    print(solution.reverseBits(43261596)) # Expected: 964176192