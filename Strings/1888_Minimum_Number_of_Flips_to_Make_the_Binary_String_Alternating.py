# Problem: 1888. Minimum Number of Flips to Make the Binary String Alternating
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description

# Time Complexity: O(N) - We slide a window over a virtual string of length 2N exactly once
# Space Complecity: O(1) - We only track integer counters, using modulo for virtual string doubling

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        # We track the current number of differences for both possible targets: "1010..." and "0101..."
        diff1, diff2 = 0, 0
        min_flips = float('inf')

        # We simulate a doubled string (length 2N) to cover all possible Type-1 cyclic shifts
        for i in range(2 * n):
            # We use modulo to wrap around the original string
            char = s[i % n]

            # We determine what the alternating characters SHOULD be at this absolute index 'i'
            exp1 = '1' if i % 2 == 0 else '0'
            exp2 = '0' if i % 2 == 0 else '1'

            # If our sliding window has grown larger than the original string length 'n',
            # we must remove the character that just fell off the left side of the window
            if char != exp1: diff1 += 1
            if char != exp2: diff2 += 1


            # Once our window reaches the exact length 'n', we can start the minimum flips seen
            if i >= n:
                left_char = s[(i - n) % n]
                left_exp1 = '1' if (i- n) % 2 == 0 else '0'
                left_exp2 = '0' if (i - n) % 2 == 0 else '1'

                if left_char != left_exp1: diff1 -= 1
                if left_char != left_exp2: diff2 -= 1

            if i >= n - 1:
                min_flips = min(min_flips, diff1, diff2)

        return min_flips
    

# ---------------------------------------------------
# Local Test Area  
if __name__ == "__main__":
    sol = Solution()

    # Test 1: S = "111000", Shift 1 to end -> "110001", Flip 2 bits -> "101010"
    print(f"Test 1: {sol.minFlips("111000")}") # Expected: 2
    
    # Test 2: S = "010", Already alternating
    print(f"Test 2: {sol.minFlips('010')}") # Expected: 0
    
    # Test 3: S = "1110", Shift and flip
    print(f"Test 3: {sol.minFlips('1110')}") # Expected: 1