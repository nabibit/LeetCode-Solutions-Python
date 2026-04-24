# Problem: 2833. Furthest Point From Origin
# Difficulty: Easy
# Link: https://leetcode.com/problems/furthest-point-from-origin/description

# Time Complexity: O(N) - We scan the string to count the charactes.
# Space Complexity: O(1) - We only store the integer counts.

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Calculate the net distance moved by explcit L and R commands
        base_distance = abs(moves.count('L') - moves.count('R'))

        # All wildcars (_) should greedly be applied to our dominant direction
        wildcards = moves.count('_')

        return base_distance + wildcards
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Leaning Right
    print(f"Test 1: {sol.furthestDistanceFromOrigin('L_RL__R')}") 
    # Expected: 3 
    # (L=2, R=2, _=3. Base distance = 0. Add wildcards = 3. Turn all '_' to 'R' or 'L'.)
    
    # Test 2: Leaning Left
    print(f"Test 2: {sol.furthestDistanceFromOrigin('_R__LL_')}") 
    # Expected: 5 
    # (L=2, R=1, _=4. Base distance = 1. Add wildcards = 5. Turn all '_' to 'L'.)
    
    # Test 3: Only Wildcards
    print(f"Test 3: {sol.furthestDistanceFromOrigin('_______')}") 
    # Expected: 7