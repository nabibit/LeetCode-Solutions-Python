# Problem: 3723. Maximize Sum of Squares of Digits
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

# Time Complexity: O(N) - Where N is 'num'. The mathematical evaluation is O(1), and constructing the resulting string of length N takes O(N) time.
# Space Complexity: O(N) - We allocate memory to store the final string of length N. Auxiliary logic uses strictly O(1) space.

class Solution:
    def maximizeSumOfSquares(self, num: int, sum_val: int) -> str:
        # Step 1: Base boundary checks
        if sum_val < 1 or sum_val > 9 * num:
            return ""
            
        # Step 2: Calculate the exact distribution of extreme digits
        nines_count = sum_val // 9
        remainder = sum_val % 9
        
        # If the sum perfectly maxes out every single digit
        if nines_count == num:
            return "9" * num
            
        # Step 3: Calculate required trailing zeros to fulfill the length constraint
        zeros_count = num - nines_count - 1
        
        # Step 4: Construct the globally optimal string
        return ("9" * nines_count) + str(remainder) + ("0" * zeros_count)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard breakdown
    print(f"Test 1: {sol.maximizeSumOfSquares(3, 20)}") 
    # Expected: "992" 
    # (Two 9s = 18, remainder 2, zero 0s. 9^2 + 9^2 + 2^2 = 166. Largest possible!)
    
    # Test 2: Needs padding
    print(f"Test 2: {sol.maximizeSumOfSquares(4, 10)}") 
    # Expected: "9100"
    
    # Test 3: Impossible target
    print(f"Test 3: {sol.maximizeSumOfSquares(2, 19)}") 
    # Expected: ""