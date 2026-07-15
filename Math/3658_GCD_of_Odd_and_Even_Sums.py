# Problem: 3658. GCD of Odd and Even Sums
# Difficulty: Easy
# Link: https://leetcode.com/problems/gcd-of-odd-and-even-sums/description

# Time Complexity: O(1) - Pure mathematical resolution taking constant time.
# Space Complexity: O(1) - No auxiliary space used.

class Solution:
    def gcdOfOddAndEvenSums(self, n: int) -> int:
        # Mathematical Proof:
        # The sum of the first 'n' odd numbers is exactly n^2
        # The sum of the first 'n' even numbers is exactly n * (n + 1)
        # We need GCD(n^2, n * (n + 1)).
        # Factoring out n gives: n * GCD(n, n + 1).
        # Since n and (n + 1) are consecutive integers, they are always coprime (their GCD is 1).
        # Therefore, n * 1 = n. The answer is always just n!
        return n

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n = 1
    # Odd sum: 1. Even sum: 2. GCD(1, 2) = 1
    print(f"Test 1: {sol.gcdOfOddAndEvenSums(1)}") 
    # Expected: 1
    
    # Test 2: n = 4
    # Odd sum: 1+3+5+7 = 16. Even sum: 2+4+6+8 = 20. GCD(16, 20) = 4
    print(f"Test 2: {sol.gcdOfOddAndEvenSums(4)}") 
    # Expected: 4
    
    # Test 3: Massive constraint (simulating n = 10^5)
    print(f"Test 3: {sol.gcdOfOddAndEvenSums(100000)}") 
    # Expected: 100000