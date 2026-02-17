# Problem: Longest Balanced Substring II
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-balanced-substring-ii/description/

# Time Complexity: O(N) - We iterate through the string a constant number of times (Solos + 3 Pairs + 1 Trio)
# Space Complexity: O(N) - The hash map for prefix differences can store up to N entries

from typing import List, Optional, Tuple, Dict

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        n = len(s)

        # Case 1: Solos (Single characters)
        # We check for the longest run of "aaaa", "bb", etc.
        current_run = 0
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                current_run += 1
            else:
                current_run = 1
            
            if current_run > max_len:
                max_len = current_run

        # Case 2: Duos (Pairs)
        # We check {a,b}, {b,c}, {a,c}. Any third char resets the chain
        pairs = [('a', 'b'), ('b', 'c'), ('a', 'c')]

        for char1, char2 in pairs:
            # We map difference -> first_index
            # We use {0: -1} to handle cases starting from the very beginning
            diff_map = {0: -1}
            diff = 0

            for i in range(n):
                char = s[i]
                if char == char1:
                    diff += 1
                elif char == char2:
                    diff -= 1
                else:
                    # Reset: The chain breals. The current index 'i' becomes the
                    # new "zero point" for the next potential chain
                    diff_map = {0: i}
                    diff = 0
                    continue

                if diff in diff_map:
                    length = i - diff_map[diff]
                    if length > max_len:
                        max_len = length
                else:
                    diff_map[diff] = i

        # Case 3: Trios (All three)
        # We need count(a) == count(b) == count(c)
        # We track (a-b, b-c)
        diff_map = {(0,0): -1}
        c_a = 0
        c_b = 0
        c_c = 0

        for i in range(n):
            if s[i] == 'a': c_a += 1
            elif s[i] == 'b': c_b += 1
            elif s[i] == 'c': c_c += 1

            diff1 = c_a - c_b
            diff2 = c_b - c_c
            key = (diff1, diff2)

            if key in diff_map:
                length = i - diff_map[key]
                if length > max_len:
                    max_len = length
            else:
                diff_map[key] = i

        return max_len
    

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    test_1 = "aabbab" # Expected: 6
    test_2 = "aaabbbccc" # Expected: 9
    test_3 = "abc" # Expected: 3
    
    print(f"Test 1 (aabbab): {solution.longestBalanced(test_1)}")
    print(f"Test 2 (aaabbbccc): {solution.longestBalanced(test_2)}")
    print(f"Test 3 (abc): {solution.longestBalanced(test_3)}")