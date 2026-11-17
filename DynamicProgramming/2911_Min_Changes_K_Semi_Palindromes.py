# Problem: 2911. Minimum Changes to Make K Semi-palindromes
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

# Time Complexity: O(N^3 + N^2 * K) - Precomputing the costs takes roughly O(N^3) since we check bounded divisors for O(N^2) substrings. The DP partition sweep takes O(N^2 * K).
# Space Complexity: O(N^2 + N * K) - We allocate an N x N matrix for the precomputed costs and an N x K matrix for the DP state.

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute all valid divisors up to length N to save time later
        divisors = {l: [] for l in range(1, n + 1)}
        for d in range(1, n):
            for l in range(d * 2, n + 1, d):
                divisors[l].append(d)
                
        # Precompute the minimum cost to make any substring s[i:j+1] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            # Substrings must be at least length 2 to have a valid divisor d < length
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                # Check every valid divisor for this specific substring length
                for d in divisors[length]:
                    changes = 0
                    
                    # Check the 'd' interwoven groups
                    for offset in range(d):
                        left = i + offset
                        # Fast-forward the right pointer to the last element in this specific interwoven group
                        right = i + offset + ((length - 1 - offset) // d) * d
                        
                        # Standard two-pointer palindrome check, but stepping by 'd'
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                            
                    min_changes = min(min_changes, changes)
                    
                cost[i][j] = min_changes
                
        # DP to find the minimum cost to partition s into exactly k semi-palindromes
        # dp[i][p] = min cost to partition first 'i' characters into 'p' groups
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for p in range(1, k + 1):
                # We need a previous cut 'm'. The new substring is s[m:i].
                # It must be at least length 2, so m can be at most i - 2.
                for m in range(i - 1):
                    if dp[m][p - 1] != float('inf') and cost[m][i - 1] != float('inf'):
                        dp[i][p] = min(dp[i][p], dp[m][p - 1] + cost[m][i - 1])
                        
        return dp[n][k]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard partition
    print(f"Test 1: {sol.minimumChanges('abcac', 2)}") 
    # Expected: 1 
    # (Split into "ab" and "cac". "ab" needs 1 change to become "aa". "cac" is already a palindrome).
    
    # Test 2: Perfect semi-palindrome requires no changes
    print(f"Test 2: {sol.minimumChanges('abcdef', 2)}") 
    # Expected: 2