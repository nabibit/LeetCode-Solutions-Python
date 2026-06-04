# Problem: 3751. Total Waviness of Numbers in Range I
# Difficulty: Medium
# Link: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description

# Time Complexity: O(log(num2)) - The time scales with the number of DIGITS in num2, not the value itself. The DP state space is tiny (Index * 2 * 2 * 11 * 11).
# Space Complexity: O(log(num2)) - The recursion stack and memoization dictionary only grow as deep as the number of digits.

from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        # Helper to find total waviness in range [0, num]
        def count_waves(num_str: str) -> int:
            
            # Returns a tuple: (count_of_valid_suffixes, total_waviness_in_those_suffixes)
            @cache
            def dp(idx: int, is_bound: bool, is_lead: bool, p1: int, p2: int):
                # Base Case: We successfully built a complete number
                if idx == len(num_str):
                    return (1, 0)
                    
                # If we are bound by the prefix, we can't exceed the target's digit at this index
                limit = int(num_str[idx]) if is_bound else 9
                total_count = 0
                total_wav = 0
                
                # Try placing every valid digit at the current position
                for d in range(limit + 1):
                    nxt_bound = is_bound and (d == limit)
                    nxt_lead = is_lead and (d == 0)
                    
                    # Update our rolling window of the last 2 digits
                    if nxt_lead:
                        nxt_p1, nxt_p2 = -1, -1
                    else:
                        nxt_p1, nxt_p2 = d, p1
                        
                    # Check if the digit we just locked in (p1) forms a wave
                    is_wave = 0
                    if p1 != -1 and p2 != -1 and not nxt_lead:
                        # Peak: p2 < p1 > d
                        # Valley: p2 > p1 < d
                        if (p2 < p1 and p1 > d) or (p2 > p1 and p1 < d):
                            is_wave = 1
                            
                    # Recursively calculate the rest of the digits
                    cnt, wav = dp(idx + 1, nxt_bound, nxt_lead, nxt_p1, nxt_p2)
                    
                    total_count += cnt
                    # The total waviness is the waviness from the suffixes, PLUS
                    # our newly formed wave multiplied by how many suffixes exist
                    total_wav += wav + (is_wave * cnt)
                    
                return (total_count, total_wav)
                
            return dp(0, True, True, -1, -1)[1]

        # F(num2) - F(num1 - 1) gives us the exact count for the inclusive range [num1, num2]
        return count_waves(str(num2)) - count_waves(str(num1 - 1))

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Small range where only 101 to 109 form a valley
    print(f"Test 1: {sol.totalWaviness(100, 110)}") 
    # Expected: 9
    # (101, 102, 103, 104, 105, 106, 107, 108, 109 all have '0' as a valley)
    
    # Test 2: Double wave (e.g., 1212)
    print(f"Test 2: {sol.totalWaviness(1212, 1212)}") 
    # Expected: 2
    # (1212 has a peak at 2, and a valley at 1)