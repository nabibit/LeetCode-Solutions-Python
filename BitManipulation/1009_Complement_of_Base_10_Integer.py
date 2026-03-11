# Problem: 1009. Complement of Base 10 Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/complement-of-base-10-integer/description

# Time Complexity: O(1) - We use built-in bit length calculation and a single XOR operation
# Space Complexity: O(1) - We only use a few integer variables

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Edge case: The problem specifies the complement of 0 is 1
        if n == 0:
            return 1
        
        # We find out exactly how many bits are in our number
        # For example, 5 is "101", which has a length of 3
        length = n.bit_length()

        # We create a "mask" of all 1s that is the same length as our number
        # Shifting 1 left by 'length' gives us 1 followed by 'length' zeros (e.g., 1000 for length 3)
        # Substracting 1 flips all those zeros to 1s (e.g., 1000 - 1 = 0111)
        mask = (1 << length) - 1

        # We XOR our original number with the mask of all 1s
        # XORing any bit with a 1 perfectly flips it (0 becomes 1, 1 becomes 0)
        return n ^ mask
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n = 5 ("101")
    print(f"Test 1: {sol.bitwiseComplement(5)}") # Expected: 2 ("010")
    
    # Test 2: n = 7 ("111")
    print(f"Test 2: {sol.bitwiseComplement(7)}") # Expected: 0 ("000")
    
    # Test 3: n = 0 ("0")
    print(f"Test 3: {sol.bitwiseComplement(0)}") # Expected: 1 ("1")