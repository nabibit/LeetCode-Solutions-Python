# Problem: 1022. Sum of Root To Leaf Binary Numbers
# Difficutly: Easy
# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description

# Time Complexity: O(N) - We visit every node in the tree exactly once
# Space Complexity: O(H) - We utilize O(H) memory for the recursion stack, where H is the tree height

from typing import Optional
import collections

# Definition for a binary tree
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            # We shift the current sum left by 1 (multiply by 2) and add the current node's bit
            current_sum = (current_sum << 1) | node.val

            # We return the fully formed number if we reach leaf node
            if not node.left and not node.right:
                return current_sum

            # We recursively calculate and sum the values from the left and right branches
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        # We initiate the depth-first search starting from the root with an initial sum of 0
        return dfs(root, 0)
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    def build_tree(values: list) -> Optional[TreeNode]:
        """Helper to build a tree from LeetCode's level-order array format."""
        if not values: return None
        root = TreeNode(values[0])
        queue = collections.deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    solution = Solution()
    
    # Test 1: [1,0,1,0,1,0,1]
    # Paths: 100(4), 101(5), 110(6), 111(7) -> Sum = 22
    tree1 = build_tree([1, 0, 1, 0, 1, 0, 1])
    print(f"Test 1: {solution.sumRootToLeaf(tree1)}") # Expected: 22
    
    # Test 2: [0]
    # Path: 0 -> Sum = 0
    tree2 = build_tree([0])
    print(f"Test 2: {solution.sumRootToLeaf(tree2)}") # Expected: 0