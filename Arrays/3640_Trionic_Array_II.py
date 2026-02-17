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
        
        # "prev" variables hold the state of index i - 1
        # We initialize them as if we are standing at index 0
        prev_inc1_sum = nums[0] # The sum of the first ascent ending at index 0
        prev_inc1_len = 1 # The length is 1 because it includes the first element

        prev_dec_sum = float('-inf') # No descent can end at index 0
        prev_dec_len = 0 

        prev_inc2_sum = float('-inf') # No final ascent can end at index 0

        # We start the global max at -infinity to ensure we don't accidentally return 0
        # if the actual best answer is a negative number (e.g., -4)
        global_max = float('-inf')

        for i in range(1, n):
            curr = nums[i]
            prev = nums [i-1]

            # Temporary variables to calculate the new state for index i based on the previous state at index i-1
            # We must store results in temporary variable first
            # If we updated "prev_" directly, we would lose the history
            # needed for other calculations at the same index

            # Default: If not extending, reset to just the current element (resting)
            curr_inc1_sum = curr
            curr_inc1_len = 1

            
            # Default: If not valid, stays -inf
            curr_dec_sum = float('-inf')
            curr_dec_len = 0
            curr_inc2_sum = float('-inf')

            # First Ascent: UP
            if curr > prev:
                # Option A: Extend the current climb
                extend_sum = prev_inc1_sum + curr

                # Option B: Start a Fresh climb here
                # This is crucial for handling negative prefixes
                # If "prev + curr" is better then the whole history , we restart
                fresh_sum = prev + curr
                
                if fresh_sum > extend_sum:
                    curr_inc1_sum = fresh_sum
                    curr_inc1_len = 2 # Length is 2 because we used (prev, curr)

                else:
                    curr_inc1_sum = extend_sum
                    curr_inc1_len = prev_inc1_len + 1
                
                # If curr <= prev, curr_inc1 defaults to "curr" (rested) defined above, so we don't need an else case here

            # Descent: DOWN
            if curr < prev:
                # Try to extend an existing descent
                if prev_dec_sum != float('-inf'):
                    curr_dec_sum = prev_dec_sum + curr
                    curr_dec_len = prev_dec_len + 1
                else:
                    curr_dec_sum = float('-inf')
                    curr_dec_len = 0

                # Try to start a new descent from a valid Peak
                # To be a valid peak, the ascent must have had at least 2 steps
                if prev_inc1_len >= 2:
                    pnd = prev_inc1_sum + curr
                    if pnd > curr_dec_sum:
                        curr_dec_sum = pnd
                        curr_dec_len = 2

            # Final Ascent: UP
            if curr > prev:
                # Try to extend an existing final ascent
                if prev_inc2_sum != float('-inf'):
                    curr_inc2_sum = prev_inc2_sum + curr

                # try to start the final ascent from a valid Valley
                # To be a valid valley, the descent must have had at least 2 steps
                if prev_dec_len >= 2:
                    pnf = prev_dec_sum + curr
                    if pnf > curr_inc2_sum:
                        curr_inc2_sum = pnf

            # We check if the current completed shape is the best we've seen so far
            if curr_inc2_sum > global_max:
                global_max = curr_inc2_sum

            # The Handover
            # Now that all calculations for index i are done, 
            # we update the "prev_" variables to be the current state for the next iteration
            prev_inc1_sum , prev_inc1_len = curr_inc1_sum, curr_inc1_len
            prev_dec_sum, prev_dec_len = curr_dec_sum, curr_dec_len
            prev_inc2_sum = curr_inc2_sum

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