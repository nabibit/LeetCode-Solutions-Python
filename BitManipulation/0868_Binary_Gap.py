# Problem: 868. Binary Gap
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-gap/description

# Time Complexity: O(log N) - We shift the number right one bit at a time
#                   An integer N has roughly log2(N) bits, so the loop runs at most 32 times.
# Space Complexity: O(1) - We only use three integer variables, using zero extra memory

class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = -1
        current_pos = 0

        # Keep checking until we've shifted away all the 1s
        while n > 0:
            # Check is the absolute rightmost bit is a 1
            if n & 1 == 1:
                # If we have seen a 1 before, measure the distance
                if last_pos != -1:
                    max_gap = max(max_gap, current_pos - last_pos)

                last_pos = current_pos

            # Shift all bits to the right by 1 (effectively dividing by 2)
            n >>= 1
            current_pos += 1

        return max_gap 
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: n = 22 (Binary: 10110)
    # 1s are at positions 1, 2, and 4.
    # Gap between pos 1 and 2 is 1. Gap between pos 2 and 4 is 2.
    print(f"Test 1 (22): {solution.binaryGap(22)}") # Expected: 2
    
    # Test 2: n = 8 (Binary: 1000)
    # Only one 1, so no adjacent pairs.
    print(f"Test 2 (8): {solution.binaryGap(8)}")   # Expected: 0
    
    # Test 3: n = 5 (Binary: 101)
    # 1s are at positions 0 and 2. Gap is 2.
    print(f"Test 3 (5): {solution.binaryGap(5)}")   # Expected: 2