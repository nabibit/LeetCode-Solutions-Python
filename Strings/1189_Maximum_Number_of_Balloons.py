# Problem: 1189. Maximum Number of Balloons
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-number-of-balloons/description

# Time Complexity: O(N) - We perform a single pass through the string of length N to count character frquencies.
# Space Complexity: O(1) - The frequency hash map stores at most 26 lowercase English letters, which  is strictly constant auxiliary space.

from collections import Counter 

class Solution:
    # Generate an O(N) frquency map of the text
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)

        # To form the word "balloon" we require:
        # 1x 'b', 1x 'a', 2x 'l', 2x 'o', 1x 'n'
        # We scale down the double-characters by 2, and find our scarcest resource
        return min(
            cnt['b'],
            cnt['a'],
            cnt['l'] // 2,
            cnt['o'] // 2,
            cnt['n']
        )
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard single instance
    print(f"Test 1: {sol.maxNumberOfBalloons('nlaebolko')}") 
    # Expected: 1
    
    # Test 2: Double instance scattered
    print(f"Test 2: {sol.maxNumberOfBalloons('loonbalxballpoon')}") 
    # Expected: 2
    
    # Test 3: Plenty of chars, but missing the double 'l's
    print(f"Test 3: {sol.maxNumberOfBalloons('leetcode')}") 
    # Expected: 0