# Problem: 3756. Concatenate Non-Zero Digits and Multiply by Sum II
# Difficulty: Medium
# Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/description

# Time Complexity: O(M + Q log M) - Precomputing prefixes takes O(M) time where M is the length of the string. Answering Q queries takes O(log M) time each using binary search.
# Space Complexity: O(M) - We store the non-zero indices, digits, and prefix math arrays in auxiliary memory.

import bisect
from typing import List

class Solution:
    def concatenateAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Extract non-zero digits and track their original 0-based indices
        indices = []
        digits = []
        for i, char in enumerate(s):
            if char != '0':
                indices.append(i)
                digits.append(int(char))
                
        k = len(digits)
        
        # Build modular prefix arrays for the non-zero digits
        pref_sum = [0] * (k + 1)
        pref_val = [0] * (k + 1)
        pow10 = [1] * (k + 1)
        
        for i in range(k):
            pref_sum[i+1] = pref_sum[i] + digits[i]
            pref_val[i+1] = (pref_val[i] * 10 + digits[i]) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD
            
        # Process each range query using binary search
        ans = []
        for l, r in queries:
            # Find the slice of non-zero digits that fall within [l, r]
            L = bisect.bisect_left(indices, l)
            R = bisect.bisect_right(indices, r) - 1
            
            if L > R:
                # No non-zero digits exist in this range
                ans.append(0)
            else:
                length = R - L + 1
                
                # Extract the concatenated integer value x in O(1) time
                x = (pref_val[R+1] - pref_val[L] * pow10[length]) % MOD
                
                # Extract the digit sum in O(1) time
                digit_sum = pref_sum[R+1] - pref_sum[L]
                
                # Multiply and apply modulo
                res = (x * (digit_sum % MOD)) % MOD
                ans.append(res)
                
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Mixed zeros and non-zeros
    print(f"Test 1: {sol.concatenateAndMultiply('030450201', [[1, 6], [0, 2]])}") 
    # Expected: [48328, 9]
    
    # Test 2: All zeros in range
    print(f"Test 2: {sol.concatenateAndMultiply('00000', [[0, 4]])}") 
    # Expected: [0]