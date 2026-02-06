# Problem: 3013. Divide an Array Into Subarrays With Minimum Cost II
# Difficulty: Hard
# Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

# Time Complexity: O(N log D)
# - We iterate through the array once (O(N)).
# - Heap operations take O(log D), where D is the window size (dist)
# Space Complexity: O(N)
# - In the worst case of "lazy removal" (many deleted items not yet popped), the heap size can grow to O(N)

from typing import List
import heapq

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Base cost always includes the first element (Start of Subarray 1)
        cost_fixed = nums[0]
        n = len(nums)

        # We need to select k-1 cut points total (excluding index 0)
        # One is the "Vice-Captain" (index i)
        # The other k-2 must come from the window [i+1, i+dist]
        target_count = k - 2

        # Edge Case: If k=2, we don't need any extra numbers from the window
        # We just need the minimum of the rest of the array
        if target_count == 0:
            return cost_fixed + min(nums[1:])

        # Dual Heap "Window Manager"
        # left_heap: Max-Heap (simulated with negative values) for the smallest 'target_count' elements
        # right_heap: Min-Heap for the larger numbers
        left_heap = []
        right_heap = []

        left_sum = 0
        left_count = 0 # Actual count of valid elements in left_heap

        # "Lazy Removal" tracker: Maps value -> count of instances to remove
        delayed_removals = {}

        def mark_for_removal(val):
            delayed_removals[val] = delayed_removals.get(val, 0) + 1
        def clean_heap(heap, is_min_heap=True):
            # Pops elements from the top if they are marked for removal
            while heap:
                val = heap[0] if is_min_heap else -heap[0]
                if val in delayed_removals and delayed_removals[val] > 0:
                    delayed_removals[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal left_sum, left_count
            # Ensure heaps are clean at the top before peeking/moving
            clean_heap(left_heap, is_min_heap=False)
            clean_heap(right_heap, is_min_heap=True)

            # If Left has too many, move largest to Right
            while left_count > target_count:
                val = -heapq.heappop(left_heap)
                heapq.heappush(right_heap, val)
                left_sum -= val
                left_count -= 1
                clean_heap(left_heap, is_min_heap=False)

            # If Left has too few (and Right has available), move smallest from Right to Left
            while left_count < target_count and right_heap:
                val = heapq.heappop(right_heap)
                heapq.heappush(left_heap, -val)
                left_sum += val
                left_count += 1
                clean_heap(right_heap, is_min_heap=True) # Clean after popping

        def add_number(val):
            nonlocal left_sum, left_count
            # Decide which heap gets the new number
            # If it's smaller then the largest in Left, it belongs in Left
            if not left_heap or val < -left_heap[0]:
                heapq.heappush(left_heap, -val)
                left_sum += val
                left_count += 1
            else:
                heapq.heappush(right_heap, val)
            balance()

        def remove_number(val):
            nonlocal left_sum, left_count
            # Check if the number to remove is likely in Left
            # (We need to clean first to trust the top element)
            clean_heap(left_heap, is_min_heap=False)

            if left_heap and val <= -left_heap[0]:
                left_sum -= val
                left_count -= 1

            mark_for_removal(val)
            balance()

        # Initilaization
        # Fill the window with the first position
        # Start the 2nd subarray at index 1
        # Window for remaining k-2 elements is nums [2] ... nums[dist+1]
        max_init_idx = min(len(nums), dist + 2)
        for val in nums[2:max_init_idx]:
            add_number(val)

        # Initial Minimum Cost (Start at 0 + Start at 1 + Sum of k-2 smallest in window)
        min_total_cost = cost_fixed + nums[1] + left_sum

        # Slinding Window Loop
        # i is the index of  the 2nd subarray start (Vice-Captain)
        # But as the "Vice-Captain" moves to i+1, this number leaves the window
        # (it becomes the Vice-Captain itself)
        for i in range(1, n - 1):
            remove_number(nums[i+1])

            # A new number enters the window from the far right: nums[i + 1 + dist]
            next_incoming_idx = i + 1 + dist
            if next_incoming_idx < n:
                add_number(nums[next_incoming_idx])

            # Calculate cost for the NEW setup where Vice-Captain is at index i+1
            # We only record cost if we have enough elements in Left Heap
            if left_count == target_count:
                current_cost = cost_fixed + nums[i+1] + left_sum
                min_total_cost = min(min_total_cost, current_cost)

        return min_total_cost
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Standard
    # nums=[1,3,2,6,4,2], k=3, dist=3
    # Fixed: 1. Need 2 more. Window size 3.
    # If Vice=3 (idx 1): Window [2,6,4]. Smallest k-2 (1) is 2. Cost: 1+3+2 = 6.
    # If Vice=2 (idx 2): Window [6,4,2]. Smallest 1 is 2. Cost: 1+2+2 = 5. (Winner)
    nums1 = [1,3,2,6,4,2]
    k1 = 3
    dist1 = 3
    expected_1 = 5
    result_1 = solution.minimumCost(nums1, k1, dist1)
    print(f"Test 1: {result_1 == expected_1} | Got: {result_1} | Expected: {expected_1}")

    # Test Case 2: Minimal k (k=2)
    # Just need 1 (fixed) + 1 smallest from rest.
    # 10 is fixed. Smallest of [1,2,2,2] is 1. Total 11.
    nums2 = [10, 1, 2, 2, 2]
    k2 = 2
    dist2 = 2
    expected_2 = 11
    result_2 = solution.minimumCost(nums2, k2, dist2)
    print(f"Test 2: {result_2 == expected_2} | Got: {result_2} | Expected: {expected_2}")

    # Test Case 3: Tight constraints
    # nums=[1,5,3,7], k=3, dist=1. 
    # Fixed 1. 
    # i=1 (5): Window [3]. Smallest 1 is 3. Cost 1+5+3 = 9.
    # i=2 (3): Window [7]. Smallest 1 is 7. Cost 1+3+7 = 11.
    nums3 = [1, 5, 3, 7]
    k3 = 3
    dist3 = 1
    expected_3 = 9
    result_3 = solution.minimumCost(nums3, k3, dist3)
    print(f"Test 3: {result_3 == expected_3} | Got: {result_3} | Expected: {expected_3}")