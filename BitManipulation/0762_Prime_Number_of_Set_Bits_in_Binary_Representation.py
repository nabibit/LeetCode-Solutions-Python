# Problem: 762. Prime Number of Set Bits in Binary Representation
# Difficulty: Easy
# Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description

# Time Complexity: O(N) - We iterate through the range once. Counting bits and checking the set takes O(1) time.
# Space Complexity: O(1) - We only store a tiny, fixed-size set of prime numbers.
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # We hardcode the primes up to 19.
        # The maximum value is 10^6, which takes at most 20 bits in binary
        # Therefore, the maximum possible set bits is 20
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        valid_count = 0

        # We iterate through every number in the inclusive range
        for i in range(left, right + 1):
            # i.bit_count() is a highly optimized C-level function in Python
            # that counts the '1's in the binary representation            
            if i.bit_count() in primes:
                valid_count += 1

        return valid_count
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Range [6, 10]
    # 6  -> 110 (2 bits, prime) -> YES
    # 7  -> 111 (3 bits, prime) -> YES
    # 8  -> 1000 (1 bit, not prime) -> NO
    # 9  -> 1001 (2 bits, prime) -> YES
    # 10 -> 1010 (2 bits, prime) -> YES
    print(f"Test 1: {solution.countPrimeSetBits(6, 10)}") # Expected: 4
    
    # Test Case 2: Range [10, 15]
    # 10 -> 1010 (2 bits) -> YES
    # 11 -> 1011 (3 bits) -> YES
    # 12 -> 1100 (2 bits) -> YES
    # 13 -> 1101 (3 bits) -> YES
    # 14 -> 1110 (3 bits) -> YES
    # 15 -> 1111 (4 bits) -> NO
    print(f"Test 2: {solution.countPrimeSetBits(10, 15)}") # Expected: 5