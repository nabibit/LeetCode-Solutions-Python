# Problem: 3666. Minimum Operations to Equalize Binary String
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description

# Time Complexiy: O(N log N) - We use a SortedList to find and remove valid parity states efficiently
# Space Complexity: O(N) - We store the unvisited stated in a SortedList and active states in a deque
from collections import deque
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # We intialize two sorted lists to track unvisited zero-counts by parity (even/odd)
        ts = [SortedList(range(i, n + 1, 2)) for i in range(2)]
        
        cnt0 = s.count('0')
        # We remove the initial state from our unnvisited tracking
        ts[cnt0 % 2].remove(cnt0)
        q = deque([cnt0])
        ans = 0
        
        while q:
            # We process all active states at the current BFS depth
            for _ in range(len(q)):
                cur = q.popleft()

                # We return the step count if we have successfully eliminated all zeros
                if cur == 0: 
                    return ans

                # We calculate the boundaries [l, r] for the possible next zero-counts
                l, r = cur + k - 2 * min(cur, k), cur + k - 2 * max(k - n + cur, 0)

                # We select the target sorted list based on the parity of the ower bound
                t = ts[l % 2]

                # We perform a binary search to fing the starting index of valid states
                idx = t.bisect_left(l)

                # We pop all valid reachable states and append them to our queue
                while idx < len(t) and t[idx] <= r:
                    q.append(t.pop(idx))

            # We increment our operation count after processing the level
            ans += 1

        return -1
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: s = "110", k = 1 -> 1 step
    print(f"Test 1: {sol.minOperations('110', 1)}") # Expected: 1
    
    # Test 2: s = "0101", k = 3 -> 2 steps
    print(f"Test 2: {sol.minOperations('0101', 3)}") # Expected: 2