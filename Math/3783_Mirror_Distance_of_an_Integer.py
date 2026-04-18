# Problem: 3783. Mirror Distance of an Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/mirror-distance-of-an-integer/description

# Time Complexity: O(D) where D is the number of digits in n. Effectively O(1) for standard integers.
# Space Complexity: O(D) to store the string representation. Effectively O(1).
class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Convert to string, reverse it using slice notation, convert back to int, and find the absolute difference
        return abs(n - int(str(n)[::-1]))
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard number
    print(f"Test 1: {sol.mirrorDistance(123)}") 
    # Expected: 198 (123 - 321 = -198 -> abs -> 198)
    
    # Test 2: Number with trailing zeros
    print(f"Test 2: {sol.mirrorDistance(120)}") 
    # Expected: 99 (120 - 021 = 99 -> abs -> 99)
    
    # Test 3: Palindrome number
    print(f"Test 3: {sol.mirrorDistance(454)}") 
    # Expected: 0