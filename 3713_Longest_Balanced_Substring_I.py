# Problem: Longest Balanced Substring I
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-balanced-substring-i/description/

# Time Complexity: O(N^2) - We iterate through all possible substrings
# Space Complexity: O(1) - We use a fixed frquency array of size 26, which is constant space

from typing import List

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        # We iterate through every index to use it as the statring point of our substring
        for i in range(n):
            # We initialize a frequncy array for 25 lowercase English letters
            # Using a fixxed array is more perfomant than a hasmap for small alphabets
            counts = [0] * 26
            distinct_count = 0
            max_freq = 0

            # We extend the substring to the right, updating our metric incrementally
            for j in range(i, n):
                char_index = ord(s[j]) - ord('a')

                # We check if this is a new character for the current window
                if counts[char_index] == 0:
                    distinct_count += 1

                # We update the frequncy and track the maximum frqunce in the window
                counts[char_index] += 1
                max_freq = max(max_freq, counts[char_index])

                # We calculate the current window length
                current_length = j - i + 1

                # We verify if the substring is balanced
                # A balanced substring must satisfy: Length == (Distinct Count) * (Max Frequency)
                if max_freq * distinct_count == current_length:
                    max_len = max(max_len, current_length)

        return max_len
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1: "aabb" is balanced (2 'a', 2 'b'). Length 4.
    print(solution.longestBalanced("aabb")) 
    
    # Test Case 2: "aab" -> "aa" (2) or "b" (1). Max balanced is 2.
    print(solution.longestBalanced("aab"))
    
    # Test Case 3: "abc" -> Each appears 1 time. Length 3.
    print(solution.longestBalanced("abc"))