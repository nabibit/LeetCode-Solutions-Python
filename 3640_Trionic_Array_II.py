# Problem: Trionic Array II
# Difficulty: Hard
# Link: [https://leetcode.com/problems/trionic-array-ii/description/]

# Time Complexity: O(n) - [We iterate through the array exactly once, perfoming constat-time calculations at each step]
# Space Complexity: O(n) - [We use state arrays to track the max sum at each index for clarity]

from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        # We need at least 4 items to form the complete Up-Down-Up shape
        if n < 4:
            return 0
        
        # We intialize out state arrays with -infinity because the maximum sum
        # might be negative (if all numbers are negative)
        # inc1: Max sum ending at index i during the First Ascent
        # dec: Max sum ending at index i during the Descent
        # inc2: Max sum ending at index i during the Final Ascent
        inc1_sum = [float('-inf')] * n
        inc1_len = [0] * n

        dec_sum = [float('-inf')] * n
        dec_len = [0] * n

        inc2_sum = [float('-inf')] * n
        # Base Case: The first element starts our first ascent
        inc1_sum[0] = nums[0]
        inc1_len[0] = 1

        # We start the global max at -infinity to ensure we don't accidentally return 0
        # if the actual best answer is a negative number (e.g., -4)
        global_max = float('-inf')

        for i in range(1, n):
            curr = nums[i]
            prev = nums [i-1]

            # First Ascent: UP
            if curr > prev:
                # Option A: Extend the current climb
                extend_sum = inc1_sum[i-1] + curr

                # Option B: Start a Fresh climb here
                # This is crucial for handling negative prefixes
                # If "prev + curr" is better then the whole history , we restart
                fresh_sum = prev + curr
                
                if fresh_sum > extend_sum:
                    inc1_sum[i] = fresh_sum
                    inc1_len[i] = 2 # Length is 2 because we used (prev, curr)

                else:
                    inc1_sum[i] = extend_sum
                    inc1_len[i] = inc1_len[i-1] + 1

            else:
                # If we are not increasing, we just reset the potential start here
                inc1_sum[i] = curr
                inc1_len[i] = 1

            # Descent: DOWN
            if curr < prev:
                # Try to extend an existing descent
                if dec_sum[i-1] != float('-inf'):
                    dec_sum[i] = dec_sum[i-1] + curr
                    dec_len[i] = dec_len[i-1] + 1

                # Try to start a new descent from a valid Peak
                # To be a valid peak, the ascent must have had at least 2 steps
                if inc1_len[i-1] >= 2:
                    pnd = inc1_sum[i-1] + curr
                    if pnd > dec_sum[i]:
                        dec_sum[i] = pnd
                        dec_len[i] = 2

            # Final Ascent: UP
            if curr > prev:
                # Try tp extend an existing final ascent
                if inc2_sum[i-1] != float('-inf'):
                    inc2_sum[i] = inc2_sum[i-1] + curr

                # try to start the final ascent from a valid Valley
                # To be a valid valley, the descent must have had at least 2 steps
                if dec_len[i-1] >= 2:
                    pnf = dec_sum[i-1] + curr
                    if pnf > inc2_sum[i]:
                        inc2_sum[i] = pnf

            # We check if the current completed shape is the best we've seen so far
            if inc2_sum[i] > global_max:
                global_max = inc2_sum[i]

        # If global_max is still -inf, it means no valid trionic array was found
        # Otherwise, we convert it to an int and return it
        return int(global_max) if global_max != float('-inf') else 0

# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: The "Baggage" Case (Negative prefix should be dropped)
    # Expected: 988 (Starts from 202, ignoring -172)
    test_nums = [-754, 167, -172, 202, 735, -941, 992]
    result = solution.maxSumTrionic(test_nums)
    print(f"Test 1 Result: {result} (Expected: 988)")

    # Test 2: Simple Valid Case
    # Expected: 16 (1+5+2+8)
    print(f"Test 2 Result: {solution.maxSumTrionic([1, 5, 2, 8])}")