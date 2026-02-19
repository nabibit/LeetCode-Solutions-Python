# Problem: 696. Count Binary Substrings
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-binary-substrings/description

# Time Complexity: O(N) - We iterate through the string exactly once
# Space Complexity: O(1) - We only maintain three integer variables (total, prev_count, curr_count)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total_substrings = 0
        prev_count = 0
        curr_count = 1

        # We iterate through the string starting from the second character
        for i in range(1, len(s)):
            # We increment the current block count if the character matches the previous one
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                # When the character changes, we compute the valid substrings formed
                # between the previous block and the current block
                total_substrings += min(prev_count, curr_count)

                # We update the previous count to the current block's size,
                # and reset the current count for the newly encountered character
                prev_count = curr_count
                curr_count = 1

        # We process the final boundary after the loop terminates
        total_substrings += min(prev_count, curr_count)

        return total_substrings
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: "00110011"
    # Groups: [2, 2, 2, 2] -> min(2,2) + min(2,2) + min(2,2) = 2 + 2 + 2 = 6
    # Expected: 6
    print(f"Test 1: {solution.countBinarySubstrings('00110011')}") 
    
    # Test Case 2: "10101"
    # Groups: [1, 1, 1, 1, 1] -> 1 + 1 + 1 + 1 = 4
    # Expected: 4
    print(f"Test 2: {solution.countBinarySubstrings('10101')}")