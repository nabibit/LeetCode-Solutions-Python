# Problem: 2196. Create Binary Tree From Descriptions
# Difficulty: Medium
# Link: https://leetcode.com/problems/create-binary-tree-from-descriptions/description

# Time Complexity: O(N) - We iterate through the descriptions exactly twice (once to build, once to find the root).
# Space Complexity: O(N) - We store N unique nodes in a Hash Map, and up to N children in a Hash Set.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        # Build the nodes and connect the tree
        for parent_val, child_val, is_left in descriptions:
            # Create parent if it doesn't exist
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            # Create child if it doesn't exist
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Link them together
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Mark this node as a child
            children.add(child_val)
            
        # Find the Root (The only node that is never a child)
        for parent_val, _, _ in descriptions:
            if parent_val not in children:
                return nodes[parent_val]
                
        return None

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Helper function to print tree in pre-order for testing
    def print_tree(root):
        if not root: return "null"
        return f"[{root.val}, {print_tree(root.left)}, {print_tree(root.right)}]"

    # Test 1: Standard Tree
    desc1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    root1 = sol.createBinaryTree(desc1)
    print(f"Test 1: {print_tree(root1)}") 
    # Expected Root is 50.