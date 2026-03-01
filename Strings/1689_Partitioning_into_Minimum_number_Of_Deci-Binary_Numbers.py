# Problem: 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description

# Time Complexity: 0(L) - We scan the string exactly once to find the maximum character, where L is the lenght of string n
# Space Complexity: O(1) - We use zero extra memory

class Solution:
    def minPartitions(self, n: str) -> int:
        # We find the maximum character in the string
        # We then convert that single character back into an integer to return the result
        return int(max(n))
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n = "32" -> max digit is 3
    print(f"Test 1: {sol.minPartitions('32')}") # Expected: 3
    
    # Test 2: n = "82734" -> max digit is 8
    print(f"Test 2: {sol.minPartitions('82734')}") # Expected: 8
    
    # Test 3: n = "27346209830709182346" -> max digit is 9
    print(f"Test 3: {sol.minPartitions('27346209830709182346')}") # Expected: 9