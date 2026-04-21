# Problem: 1722. Minimize Hamming Distance After Swap Operations
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description

# Time Complexity: O(N + M * alpha(N)) - Where N is the length of the arrays, and M is the number of allowed swaps. alpha(N) is the Inverse Ackermann function (practically O(1)).
# Space Complexity: O(N) - We store the Union-Find structure and the element frquency maps.

from typing import List
from collections import defaultdict, Counter

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        # Path compression: point the node directly to the absolute root 
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank to keep the tree flat and fast
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        # Group all allowed swaps into connected components
        for u, v in allowedSwaps:
            uf.union(u, v)

        # Group the indices by their absolute root (their "World")
        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)

        hamming_distance = 0

        # For each isolated World, check how many numbers we can successfully watch
        for indices in components.values():
            # Count the available numbers from the 'source' arrays in this specific World
            available_numbers = Counter(source[i] for i in indices)

            # Try to satisfy the 'target' array requirements
            for i in indices:
                needed_num = target[i]
                if available_numbers[needed_num] > 0:
                    available_numbers[needed_num] -= 1 # Match succesfully
                else:
                    hamming_distance += 1 # Match failed, increase the distance

        return hamming_distance
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Full connected component allows perfect sorting
    print(f"Test 1: {sol.minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]])}") 
    # Expected: 1 
    # (Indices 0,1 are a world. We have {1,2}, we need {2,1}. Perfect match.
    #  Indices 2,3 are a world. We have {3,4}, we need {4,5}. '4' matches, '3' fails. Distance = 1)
    
    # Test 2: Transitive swaps link the whole array
    print(f"Test 2: {sol.minimumHammingDistance([1,2,3,4], [1,3,2,4], [])}") 
    # Expected: 2 (No swaps allowed, 2 and 3 are in the wrong spots)