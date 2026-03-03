# Problem: 1545. Find Kth Bit in Nth Binary String
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

# Time Complexity: O(N) - We halve the search space at each step, taking at most N steps
# Space Complexity: O(N) - We use O(N) space for the recursive call stack

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: The first sequence is always just "0"
        if n == 1:
            return "0"

        # We calculate the total length of the current sequence Sn
        # The length of Sn is exactly (2^n) - 1
        length = (1 << n) - 1
        mid = length // 2 + 1

        # If k is exactly in the middle, the problem states it is always '1'
        if k == mid:
            return "1"

        # If k is in the first half, it maps exactly to the previous sequence Sn-1
        elif k < mid:
            return self.findKthBit(n-1, k)

        # If k is in the second half, it maps to the mirrored position in Sn-1
        # The mirrored position is (length - k + 1)
        # Because the second half is inverted, we must flip the final result
        else: 
            result = self.findKthBit(n-1, length - k + 1)
            return "0" if result == "1" else "1" 

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: S3 = "0111001", 1st bit
    print(f"Test 1: {sol.findKthBit(3, 1)}") # Expected: "0"
    
    # Test 2: S4 = "011100110110001", 11th bit
    print(f"Test 2: {sol.findKthBit(4, 11)}") # Expected: "1"
    
    # Test 3: S1 = "0", 1st bit
    print(f"Test 3: {sol.findKthBit(1, 1)}") # Expected: "0"