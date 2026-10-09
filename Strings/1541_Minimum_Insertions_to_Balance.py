# Problem: 1541. Minimum Insertions to Balance a Parentheses String
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

# Time Complexity: O(N) - We perform a single linear sweep across the string of length N.
# Space Complexity: O(1) - We bypass stack structures entirely, maintaining only two integer counters regardless of string size.

class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        
        for char in s:
            if char == '(':
                # If we have an odd number of needed rights, a single ')' is stranded.
                # We must insert a ')' to complete the consecutive '))' requirement before opening a new '('.
                if needed_right % 2 != 0:
                    insertions += 1
                    needed_right -= 1
                    
                needed_right += 2
            else:
                needed_right -= 1
                
                # If we drop below 0, we have an orphaned ')'.
                # We must insert a '(' to support it. 
                # This new '(' requires two ')', and since we just consumed one, we still need one more.
                if needed_right < 0:
                    insertions += 1
                    needed_right += 2
                    
        # Total insertions are the ones we made mid-string, plus the unresolved closing brackets at the end.
        return insertions + needed_right

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Perfectly balanced
    print(f"Test 1: {sol.minInsertions('())')}") 
    # Expected: 0
    
    # Test 2: Inverted with missing brackets
    print(f"Test 2: {sol.minInsertions(')()')}") 
    # Expected: 3
    # (Insert '(' before first ')', insert ')' after first ')', insert ')' at the end)
    
    # Test 3: Standard imbalance
    print(f"Test 3: {sol.minInsertions('(()))')}") 
    # Expected: 1
    # (Needs one more ')' at the end)