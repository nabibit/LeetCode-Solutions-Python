# Problem: 940. Distinct Subsequences II
# Difficulty: Hard
# Link: https://leetcode.com/problems/distinct-subsequences-ii/

# Time Complexity: O(N) - We perform a single linear sweep across the string of length N. The array lookups take strictly O(1) time.
# Space Complexity: O(1) - We allocate a fixed integer array of size 26 for the English alphabet, maintaining an absolute constant memory footprint.

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Track the number of distinct subsequences ending with each specific character
        ends_with = [0] * 26
        total_subseq = 0
        
        for char in s:
            char_idx = ord(char) - ord('a')
            
            # The new sequences we can form is (all current sequences + the character itself)
            # To avoid duplicates, we subtract the sequences that ALREADY ended with this character
            new_added = (total_subseq + 1 - ends_with[char_idx]) % MOD
            
            # Update the counts
            ends_with[char_idx] = (ends_with[char_idx] + new_added) % MOD
            total_subseq = (total_subseq + new_added) % MOD
            
        return total_subseq

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard unique letters
    print(f"Test 1: {sol.distinctSubseqII('abc')}") 
    # Expected: 7 
    # (a, b, c, ab, ac, bc, abc)
    
    # Test 2: Repeating letters (requires duplicate subtraction)
    print(f"Test 2: {sol.distinctSubseqII('aba')}") 
    # Expected: 6
    # (a, b, ab, aa, ba, aba)
    
    # Test 3: All same letters
    print(f"Test 3: {sol.distinctSubseqII('aaa')}") 
    # Expected: 3
    # (a, aa, aaa)