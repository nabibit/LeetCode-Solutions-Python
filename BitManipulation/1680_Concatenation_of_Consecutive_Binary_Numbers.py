# Problem: 1680. Concatenation of Consecutive Binary Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description

# Time Complexity: O(N) - We loop from 1 to n exactly once
# Space Complexity: O(1) - We only mainitain a running integer total

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # We define our modulo constraint as per the problem description 
        MOD = 10**9 + 7
        result = 0

        # We iterate through every number from 1 up to n
        for i in range(1, n + 1):
            # We calculate how many binary bits the current number takes up
            length = i.bit_length()

            # We shift our current result to the left by 'length' bits to make room
            # We then use a bitwise OR (|) to append the current number 'i' into those empty zero slots
            # Finally, we apply the modulo to prevent the integer from overflowing
            result = ((result << length) | i) % MOD

        return result
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n = 1 -> "1" -> 1
    print(f"Test 1: {sol.concatenatedBinary(1)}") # Expected: 1
    
    # Test 2: n = 3 -> "1" + "10" + "11" -> "11011" -> 27
    print(f"Test 2: {sol.concatenatedBinary(3)}") # Expected: 27
    
    # Test 3: n = 12
    print(f"Test 3: {sol.concatenatedBinary(12)}") # Expected: 505379714