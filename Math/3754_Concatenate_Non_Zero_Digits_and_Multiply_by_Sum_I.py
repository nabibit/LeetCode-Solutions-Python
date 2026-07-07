# Problem: 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description

# Time Complexity: O(d) where d is the number of digits in n (or O(log n)). We iterate through the digits once.
# Space Complexity: O(d) to store the filtered string characters, which takes logarithmic space relative to n.

class Solution:
    def concatenateAndMultiply(self, n: int) -> int:
        # Convert number to string to easily inspect digits
        s = str(n)
        
        # Filter out '0' characters
        non_zero_chars = [char for char in s if char != '0']
        
        # If there are no non-zero digits, x is 0
        if not non_zero_chars:
            return 0
            
        # Concatenate back to integer x
        x = int("".join(non_zero_chars))
        
        # Calculate the sum of the non-zero digits
        digit_sum = sum(int(char) for char in non_zero_chars)
        
        # Return the final product
        return x * digit_sum

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Standard number with zeroes
    # Non-zero digits: 1, 2, 5 -> x = 125, sum = 1 + 2 + 5 = 8
    # Result: 125 * 8 = 1000
    print(solution.concatenateAndMultiply(102050))  # Expected: 1000
    
    # Test Case 2: Number with no zeroes
    # Non-zero digits: 3, 4 -> x = 34, sum = 3 + 4 = 7
    # Result: 34 * 7 = 238
    print(solution.concatenateAndMultiply(34))      # Expected: 238
    
    # Test Case 3: Number with only zeroes
    print(solution.concatenateAndMultiply(0))       # Expected: 0