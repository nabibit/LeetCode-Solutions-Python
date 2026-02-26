## Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description

# Time Complexity: 0(N) - We traverse the string exactly once
# Space Complexity: O(1) - We use two integer variables, zero extra memory.

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # We traverse the string from the least significant bit (right) up to the second bit
        # We do not process the very first bit (index 0) in this loop
        for i in range(len(s) - 1, 0, -1):
            
            # We determine the current bit's value by adding any exiting carry
            digit = int(s[i]) + carry

            if digit == 1:
                # If the value is 1 (odd), we must add 1 and the divide by 2
                # This takes exactly 2 steps, and generates a new carry of 1
                steps += 2
                carry = 1
            else:
                # If the value is 0 or 2, it is currently even
                # We simply divide vy 2 (sift by right), which takes 1 step
                # The carry remains 0 (if digits was 0) or 1 (if digit was 2)
                steps += 1

        # If we reach the most significant bit and still hold a carry, 
        # it acts as an extra bit that requires one final division step
        return steps + carry
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: "1101" (13 in decimal)
    # Steps: 13 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1 (6 steps)
    print(f"Test 1: {solution.numSteps('1101')}") # Expected: 6
    
    # Test 2: "10" (2 in decimal)
    # Steps: 2 -> 1 (1 step)
    print(f"Test 2: {solution.numSteps('10')}")   # Expected: 1
    
    # Test 3: "1" (1 in decimal)
    # Steps: Already 1 (0 steps)
    print(f"Test 3: {solution.numSteps('1')}")    # Expected: 0