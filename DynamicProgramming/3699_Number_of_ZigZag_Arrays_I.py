# Problem: 3699. Number of ZigZag Arrays I
# Difficulty: Hard
# Link: https://leetcode.com/problems/number-of-zigzag-arrays-i/description

# Time Complexity: O(N * K) - Where N is the length of the array and K is the range of available numbers (r - l + 1). We do N sweeps of size K, taking O(1) time per element using prefix/suffix sums
# Space Complexity: O(K) - We only store two 1D arrays of size K to track the previous step's UP and DOWN states

class Solution:
    def numberOfZigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        # An array of length 1 has no transitions. Any number works
        if n == 1:
            return k % MOD
            
        # An array of length 2 just requires any two DISTINCT numbers
        if n == 2:
            return (k * (k - 1)) % MOD
            
        # We map the range [l, r] to 0-indexed buckets [0, k - 1]
        # For an array of length 2 ending at value 'j':
        # - It went UP if the first number was strictly less than 'j' (j choices)
        # - It went DOWN if the first number was strictly greater than 'j' (k - 1 - j choices).
        up = [j for j in range(k)]
        down = [k - 1 - j for j in range(k)]
        
        # Build the array element by element up to length N
        for _ in range(3, n + 1):
            new_up = [0] * k
            new_down = [0] * k
            
            # To make an UP step ending at 'j', the previous step MUST have gone DOWN
            # to some value strictly less than 'j'. We track this via a running prefix sum
            run_down = 0
            for j in range(k):
                new_up[j] = run_down
                run_down = (run_down + down[j]) % MOD
                
            # To make a DOWN step ending at 'j', the previous step MUST have gone UP
            # to some value strictly greater than 'j'. We track this via a running suffix sum
            run_up = 0
            for j in range(k - 1, -1, -1):
                new_down[j] = run_up
                run_up = (run_up + up[j]) % MOD
                
            up = new_up
            down = new_down
            
        # The total valid ZigZag arrays is the sum of all valid UP and DOWN endings
        return (sum(up) + sum(down)) % MOD

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Small range (n=3, range [1,3])
    print(f"Test 1: {sol.numberOfZigZagArrays(3, 1, 3)}") 
    # Expected: 10 
    # (Valid arrays: [1,2,1], [1,3,1], [1,3,2], [2,1,2], [2,1,3], [2,3,1], [2,3,2], [3,1,2], [3,1,3], [3,2,3])
    
    # Test 2: Standard constraints
    print(f"Test 2: {sol.numberOfZigZagArrays(4, 1, 5)}") 
    # Expected: 170