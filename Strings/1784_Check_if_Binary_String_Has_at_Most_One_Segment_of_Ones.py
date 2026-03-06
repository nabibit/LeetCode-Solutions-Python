# Problem: 1784. Check if Binary String Has at Most One Segment of Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description

# Time Complexity: O(N) - We scan the string exactly once
# Space Complexity: O(1) - We only use a single boolean flag for memory

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
            # We track whether we have encountered a zero (gap) in our string
            seen_zero = False 

            # We iterate through each character in the binary string
            for char in s:
                if char == '0':
                        # We mark that the first contiguous segment of ones has ended
                        seen_zero = True
                elif char == '1' and seen_zero:
                        # We found a '1' after a gap, meaning a second segment has started
                        # Since the rules state "at most one", we instantly return False
                        return False
                
            # If we successfully scan the entire string without finding a second segmennt, it is valid
            return True
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Contains a gap ("01")
    print(f"Test 1: {sol.checkOnesSegment('1001')}") # Expected: False
    
    # Test 2: Only one continuous segment
    print(f"Test 2: {sol.checkOnesSegment('110')}") # Expected: True