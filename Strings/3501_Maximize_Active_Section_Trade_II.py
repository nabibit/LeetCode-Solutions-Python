# Problem: 3501. Maximize Active Section with Trade II
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximize-active-section-with-trade-ii/description

# Time Complexity: O(N log N + Q log M) - Building the Sparse Table takes O(M log M) where M is the number of zero blocks. Answering Q queries takes O(log M) time each via Binary Search.
# Space Complexity: O(N log N) - We allocate auxiliary storage for zero block metrics and the Sparse Table matrix for O(1) interval queries.

import bisect
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Prefix sum to instantly count the number of 1s in any range
        pref_ones = [0] * (n + 1)
        for i in range(n):
            pref_ones[i+1] = pref_ones[i] + (1 if s[i] == '1' else 0)
        
        # Total ones in the WHOLE string — this is the base for every query,
        # since the final answer counts active sections over all of s,
        # not just the queried substring. Only the trade itself is confined
        # to s[l..r]; everything outside stays as-is and still counts.
        total_ones = pref_ones[n]
            
        # Parse out all contiguous '0' blocks
        starts = []
        ends = []
        lengths = []
        
        i = 0
        while i < n:
            if s[i] == '0':
                st = i
                while i < n and s[i] == '0':
                    i += 1
                starts.append(st)
                ends.append(i - 1)
                lengths.append(i - st)
            else:
                i += 1
                
        m = len(lengths)
        
        # Build a Sparse Table (RMQ) for the gains of adjacent '0' blocks
        V = [lengths[k] + lengths[k+1] for k in range(m - 1)]
        ST = []
        
        if V:
            ST.append(V[:])
            step = 1
            while step * 2 <= len(V):
                prev = ST[-1]
                curr = [max(prev[j], prev[j + step]) for j in range(len(V) - step * 2 + 1)]
                ST.append(curr)
                step *= 2
                
        # Process each independent range query
        ans = []
        for l, r in queries:
            # Binary search to find intersecting zero blocks
            a = bisect.bisect_left(ends, l)
            b = bisect.bisect_right(starts, r) - 1
            
            # Case 1: No zero blocks exist in this query range
            if a > b:
                ans.append(total_ones)
                continue
                
            # Case 2: Only ONE zero block exists in this query range (Trade impossible)
            if a == b:
                ans.append(total_ones)
                continue
                
            # Case 3: Multiple zero blocks exist
            L_a = ends[a] - max(l, starts[a]) + 1
            L_b = min(r, ends[b]) - starts[b] + 1
            
            max_gain = 0
            if a + 1 == b:
                max_gain = L_a + L_b
            else:
                max_gain = max(L_a + lengths[a+1], lengths[b-1] + L_b)
                
                if a + 1 <= b - 2:
                    L_idx = a + 1
                    R_idx = b - 2
                    length_idx = R_idx - L_idx + 1
                    j = length_idx.bit_length() - 1
                    max_internal = max(ST[j][L_idx], ST[j][R_idx - (1 << j) + 1])
                    max_gain = max(max_gain, max_internal)
                    
            ans.append(total_ones + max_gain)
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard query bounds over mixed sections
    print(f"Test 1: {sol.maxActiveSectionsAfterTrade('0101010', [[0, 6], [1, 5]])}") 
    # Expected: [5, 5]
    
    # Test 2: Single zero block constraint (trade impossible)
    print(f"Test 2: {sol.maxActiveSectionsAfterTrade('01', [[0, 1]])}") 
    # Expected: [1]