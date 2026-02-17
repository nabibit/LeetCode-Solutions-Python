# Problem: 401. Binary Watch
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-watch/description

# Time Complexity: O(C(10, k)) - We visit only the valid combinations of LEDs. Max 252 iterations (for k=5)
# Space Complexity: O(k) - The recursion stack depth equals the number of LEDs turned on

from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Early pruning: Maximum LEDs that can produce valid time
        if turnedOn < 0 or turnedOn > 8:  # 3+5 = 8 is max
            return []
        
        # We prepare the result list
        result = []

        # We define the values for LEDs
        # First 4 are Hours (8, 4, 2, 1), Next 6 are Minutes (32, 16, 8, 4, 2, 1)
        # We use a single array to simplify the recursion index
        # Hours: indices 0-3, Minutes: indices 4-9
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def backtrack(index: int, count: int, current_h: int, current_m: int):
            # Base Case: If we have turned on exactly the required number of LEDs
            if count == 0:
                # We check validity: Hours must be 0-11, Minutes 0-59
                if current_h < 12 and current_m < 60:
                    result.append(f"{current_h}:{current_m:02d}")
                return 
            
            # We iterate through the remaining LEDs starting from 'index'
            # This ensures we generate combinations, not permutations (no duplicates)
            for i in range(index, 10):
                # If the remaining LEDs are fewer than we need, stop
                # (10 - i) is how many LEDs are left to pick from
                if (10 - i) < count:
                    break

                # We calculate the new time based on which LED we picked
                # If i < 4, it's an Hour LED. If i>= 4, it's a Minute LED
                if i < 4:
                    # Pruning: If adding this LED makes Hour > 11, don't explore this branch
                    if current_h + leds[i] < 12:
                        backtrack(i + 1, count - 1, current_h + leds[i], current_m)
                else:
                    # Pruning: If adding this LED makes Minute > 59, don't explore this branch
                    if current_m + leds[i] < 60:
                        backtrack(i + 1, count - 1, current_h, current_m + leds[i])

        # We start the recursion from the first LED(index 0)
        backtrack(0, turnedOn, 0, 0)
        return result
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: turnedOn = 1
    # Note: Backtracking usually finds larger values first (e.g., 8:00 before 0:01).
    # Expected (Order may vary): ["8:00", "4:00", "2:00", "1:00", "0:32", "0:16", "0:08", "0:04", "0:02", "0:01"]
    print(f"Test 1: {solution.readBinaryWatch(1)}")
    
    # Test Case 2: turnedOn = 9
    # Expected: [] (Impossible to have 9 LEDs on because max valid is 3 hours + 5 minutes = 8 LEDs)
    print(f"Test 2: {solution.readBinaryWatch(9)}")