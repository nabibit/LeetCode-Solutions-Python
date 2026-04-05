# Problem: 3474. Lexicographically Smallest Generated String
# Difficulty: Hard
# Link: https://leetcode.com/problems/lexicographically-smallest-generated-string/description

# Time Complexity: O(N + M) amortized - KMP array generation, initial overlap checks, and greedy generation with localized backtracking all run in linear time overall.
# Space Complexity: O(N + M) - We store the resulting string, KMP state arrays, and the backtracking stack.

from typing import List

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        
        word = ['?'] * L
        max_r = 0
        
        # Apply all mandatory 'T' placements optimally to stay O(N + M)
        for i in range(n):
            if str1[i] == 'T':
                start = max(i, max_r)
                for j in range(start - i, m):
                    word[i + j] = str2[j]
                max_r = max(max_r, i + m)
                
        # Build the LPS (Longest Prefix Suffix) array for str2 (Standard KMP)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and str2[i] != str2[j]:
                j = lps[j-1]
            if str2[i] == str2[j]:
                j += 1
            lps[i] = j
            
        # Verify that 'T' placements didn't create mathematical contradictions
        test_word = "".join(c if c != '?' else '#' for c in word)
        j = 0
        match_starts = set()
        for i in range(L):
            if j == m:
                j = lps[j-1]
            while j > 0 and str2[j] != test_word[i]:
                j = lps[j-1]
            if str2[j] == test_word[i]:
                j += 1
            if j == m:
                match_starts.add(i - m + 1)
                
        # If a 'T' was requested but the overlap failed, or an 'F' is unavoidably matched
        for i in range(n):
            if str1[i] == 'T' and i not in match_starts:
                return ""
            if str1[i] == 'F' and i in match_starts:
                return ""
                
        # Fill remaining '?' using Greedy KMP Automaton with localized backtracking
        is_q = [c == '?' for c in word]
        kmp_state = [0] * (L + 1)
        stack = []
        k = 0
        
        while k < L:
            # If this index was originally a wildcard, guess the smallest character
            if is_q[k]:
                if word[k] == '?':
                    word[k] = 'a'
                stack.append(k)
                
            c = word[k]
            j = kmp_state[k]
            
            # Step the KMP state machine
            if j == m:
                j = lps[j-1]
                
            while j > 0 and str2[j] != c:
                j = lps[j-1]
                
            if str2[j] == c:
                j += 1
                
            kmp_state[k+1] = j
            match_idx = k - m + 1
            
            # The Trap: Did our greedy guess accidentally complete an 'F' match?
            if j == m and 0 <= match_idx < n and str1[match_idx] == 'F':
                
                # We must change a '?' within this specific window to break the match
                if not stack or stack[-1] < match_idx:
                    return ""  # No '?' available to change, inescapable contradiction!
                    
                pos = stack.pop()
                
                # If the '?' is already 'z', we must backtrack even further
                while word[pos] == 'z':
                    word[pos] = '?' # Completely reset it for future forward passes
                    if not stack or stack[-1] < match_idx:
                        return ""
                    pos = stack.pop()
                    
                # Increment the rightmost available '?' and rewind the KMP loop to that position
                word[pos] = chr(ord(word[pos]) + 1)
                k = pos
                continue
                
            k += 1
            
        return "".join(word)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple avoiding
    print(f"Test 1: {sol.generateString('TFF', 'ab')}") 
    # Expected: "abac" (Starts with 'ab', then avoids forming 'ab' again)
    
    # Test 2: Impossible overlap contradiction
    print(f"Test 2: {sol.generateString('TT', 'aba')}") 
    # Expected: "" (T at 0 wants 'aba', T at 1 wants 'aba'. They conflict at index 1: 'b' vs 'a')