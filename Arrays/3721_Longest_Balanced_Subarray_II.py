# Problem: 3721. Longest Balanced Subarray II
# Difficulty: Hard
# Link: https://leetcode.com/problems/longest-balanced-subarray-ii/description

# Time Complexity: (O log N) - We iterate through the array once.
#                   updating the Segment Tree and querying it takes logarithmic time 
# Space Complexity: O(N) - The Segment Tree requires an array of size 4 * (N+1)
#                   and we use a Hash Map to track the last seen positions of numbers.

from typing import List

class Node:
    """
    Represents a specific range (chunk) of our Prefix Sum array.
    """
    __slots__ = ("l", "r", "mn", "mx", "lazy")
    def __init__(self):
        self.l = self.r = 0 # Left and right boundary of this chunk
        self.mn = self.mx = 0 # The Minimum and Maximum sum currently inside this chunk
        self.lazy = 0 # The "Sticky Note": stores pending +1 or -1 updates for children

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        # We initialize the Segment Tree array (Standard sizing is 4 * N)        
        tr = [Node() for _ in range((n + 1) * 4)]

        # --- Segment tree helper functions ---

        def build(u: int, l: int, r: int):
            """ Recursively divides the array to set up the boundary ranges for each node."""
            tr[u].l, tr[u].r = l, r
            if l == r: return
            mid = (l + r) // 2
            build(u * 2, l, mid)
            build(u * 2 + 1, mid + 1, r)

        def apply(u: int, v: int):
            """Instantly updates a node's Min/Max and writes the  update on its 'lazy' sticky note."""
            tr[u].mn += v
            tr[u].mx += v
            tr[u].lazy += v

        def pushdown(u: int):
            """Passes the 'lazy' sticky note down to the two direct child nodes before querying."""
            if tr[u].lazy != 0:
                apply(u * 2, tr[u].lazy)
                apply(u * 2 + 1, tr[u].lazy)
                tr[u].lazy = 0 # Clear the note once passed down

        def pushup(u: int):
            """Recalculates this node's Min/max based on the current state of its children"""
            tr[u].mn = min(tr[u *2].mn, tr[u * 2 + 1].mn)
            tr[u].mx = max(tr[u * 2].mx, tr[u * 2 + 1].mx)

        def modify(u: int, L: int, R: int, v: int):
            """Adds 'value' (+1 or -1) to all prefix sums in the range [target_left, target_right]"""
            # If this node's entire range is inside our target, apply the update lazily and stop
            if tr[u].l >= L and tr[u].r <=R:
                apply(u, v)
                return

            # Otherwise, push old updates down and split the work between children
            pushdown(u)
            mid = (tr[u].l + tr[u].r) >> 1

            if L <= mid: modify(u* 2, L, R, v)
            if R > mid: modify(u* 2 + 1, L, R, v)

            # Update the current node's min/max after children do their work
            pushup(u)

        def query(u: int, target: int) -> int:
            """Binary searches the tree to find the EARLIEST index matching the target_score."""
            # Base case: We hit a single index at the bottom of the tree
            if tr[u].l == tr[u].r: return tr[u].l
            
            pushdown(u)
            
            # Because prefix sums change only by ±1,
            # if target is within [min, max] of a segment,
            # it must exist in that segment
            # We always check the left branch first to find the EARLIEST occurrence
            if tr[u * 2].mn <= target <= tr[u * 2].mx:
                return query(u * 2, target)
            
            # If not in the left, it must be in the right branch
            return query(u * 2 + 1, target)

        # --- Main algorithm logic ---

        # Build the initial tree for indices 0 to N
        build(1, 0, n)

        last_seen = {} # Tracks the last seen index where a specific number appeared
        current_score = max_length = 0

        # We iterate starting from index 1 (Segment trees map cleanly to 1-indexed arrays)
        for i, x in enumerate(nums, start=1):

            # Odd numbers score +1, Even numbers score -1
            delta = 1 if x % 2 else -1

            # The Distinct Rule:
            # If we've seen this number before, we must "erase" its old score
            # We do this by applying the opposite of its delta from its old index to the end
            if x in last_seen:
                modify(1, last_seen[x], n, -delta)
                current_score -= delta

            # Now we record its new position and apply its score from here to the end
            last_seen[x] = i
            modify(1, i, n, delta)
            current_score += delta

            # Check: Find the earliest past index that had this exact same running score
            # A matching score means everything between that index and our current index balances out to 0
            pos = query(1, current_score)
            max_length = max(max_length, i - pos)

        return max_length
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Duplicates present. 
    # [2, 3, 2, 3] -> Distinct Evens (2) equals Distinct Odds (3). Length 4.
    print(f"Test 1: {solution.longestBalanced([2, 3, 2, 3])}") # Expected: 4
    
    # Test Case 2: No balance possible.
    # [1, 1, 1] -> Odds = 1, Evens = 0.
    print(f"Test 2: {solution.longestBalanced([1, 1, 1])}") # Expected: 0