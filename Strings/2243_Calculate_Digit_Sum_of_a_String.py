# Problem: 2243. Calculate Digit Sum of a String
# Difficulty: Easy
# Link: https://leetcode.com/problems/calculate-digit-sum-of-a-string/

# Time Complexity: O(N^2) in the absolute worst-case scenario, but practically O(N) given the constraints (N <= 100).
# Space Complexity: O(N) - We allocate a new list and string dynamically for each round , bounded by the current length of the string.
 
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # We just keep running rounds until the string is small enough to pass the length check
        while len(s) > k:
            next_round = []

            # Chop the current string into sequential blocks of size k
            for i in range(0, len(s), k):
                block = s[i:i+k]

                # Tally up the digits in this block and turn it straight back into a string
                block_sum = sum(int(digit) for digit in block)
                next_round.append(str(block_sum))

            # Mash the newly summed blocks together to form the string for the next round
            s = "".join(next_round)

        return s

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard breakdown
    print(f"Test 1: {sol.digitSum('11111222223', 3)}") 
    # Expected: "135"
    # Round 1: "111", "112", "222", "23" -> "3", "4", "6", "5" -> "3465"
    # Round 2: "346", "5" -> "13", "5" -> "135"
    
    # Test 2: Already small enough
    print(f"Test 2: {sol.digitSum('00000000', 3)}") 
    # Expected: "000"