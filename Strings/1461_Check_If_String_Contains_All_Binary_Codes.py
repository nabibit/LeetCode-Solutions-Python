# Problem: 1461. Check If a String Contains All Binary Codes of Size K
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description

# Time Complexity: O(N) where N is the length of the string s.
# Space Complexity: O(N * K) to store the substrings in the hash set.
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # The total number of unique binary codes of length k is 2^k
        # We can write this elegantly using the bitwise left shift (1 << k)
        required_count = 1 << k
        seen_codes = set()

        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            # Slice the substring and add  it to our tracking set
            seen_codes.add(s[i : i + k])
            
            # Early optimization: stop searching if we found everything
            if len(seen_codes) == required_count:
                return True

        return False
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: s = "00110110", k = 2
    # Combinations needed: 00, 01, 10, 11. All are present!
    print(f"Test 1: {solution.hasAllCodes('00110110', 2)}") # Expected: True
    
    # Test 2: s = "0110", k = 1
    # Combinations needed: 0, 1. All are present!
    print(f"Test 2: {solution.hasAllCodes('0110', 1)}")     # Expected: True
    
    # Test 3: s = "0110", k = 2
    # Combinations needed: 00, 01, 10, 11. Missing '00'.
    print(f"Test 3: {solution.hasAllCodes('0110', 2)}")     # Expected: False