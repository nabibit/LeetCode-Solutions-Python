# Problem: 1291. Sequential Digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/sequential-digits/description

# Time Complexity: O(1) - There are only exactly 36 possible sequential digit numbers in base-10 mathematics. Generating and filtering them takes strictly constant time.
# Space Complexity: O(1) - We store a fixed maximum of 36 integers in auxiliary memory.

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # The ultimate master sequence of all possible digits
        master_string = "123456789"
        ans = []
        
        # We only need to check lengths that could possibly fall within [low, high]
        low_len = len(str(low))
        high_len = len(str(high))
        
        # Slide a window of increasing lengths across the master string
        for length in range(low_len, high_len + 1):
            
            # Start index bounds ensure we don't read past the end of the 9 characters
            for start in range(10 - length):
                # Extract the sequential string and convert it to an integer
                num = int(master_string[start : start + length])
                
                # Only keep numbers that strictly fall within our target range
                if low <= num <= high:
                    ans.append(num)
                    
        # Since we generate by length, and then left-to-right, the list is naturally sorted!
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Given Example 1
    print(f"Test 1: {sol.sequentialDigits(100, 300)}") 
    # Expected: [123, 234]
    
    # Test 2: Given Example 2
    print(f"Test 2: {sol.sequentialDigits(1000, 13000)}") 
    # Expected: [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    
    # Test 3: Range encompassing multiple lengths
    print(f"Test 3: {sol.sequentialDigits(10, 1000000000)}") 
    # Will print all 36 sequential numbers starting from length 2