# Problem: 1382. Balance a Binary Search Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/balance-a-binary-search-tree/description

# Time Complexity: O(N) - We visit every node once to extract the values, and once to build the new tree.
# Space Complexity: O(N) - We store all N node values in a list, plus the recursion stack.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Harvest all the values in perfectly sorted order
        sorted_values = []

        def inorder_traversal(node):
            """Walks the tree (Left, Node, Right) to extract sorted values."""
            if not node:
                return

            inorder_traversal(node.left)
            sorted_values.append(node.val)
            inorder_traversal(node.right)        
        inorder_traversal(root)

        # Step 2: Rebuild a perfectly balanced tree from the sorted list
        def build_balanced_tree(left_idx: int, right_idx: int) -> TreeNode:
            """Recursively builds a balanced BST by always picking the middle element."""
            # Base case: if the pointers cross, there are no more numbers for this branch
            if left_idx > right_idx:
                return None

            # Find the exact middle of our current array slice
            mid = (left_idx + right_idx) // 2

            # The middle value becomes the root of this current subtree
            current_root = TreeNode(sorted_values[mid])

            # Recursively build the left side (using the left half of the slice)
            current_root.left = build_balanced_tree(left_idx, mid - 1)

            # Recursively build the right side (using the right half of the slice)
            current_root.right = build_balanced_tree(mid + 1, right_idx)

            return current_root

        # Kick off the rebuild using the entire range of our sorted list
        return build_balanced_tree(0, len(sorted_values) - 1)
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    import collections

    # Helper function to print the tree level-by-level (like LeetCode does)
    def print_level_order(root: TreeNode) -> str:
        if not root:
            return "[]"
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        # Clean up all the trailing "null"s at the bottom of the tree
        while result and result[-1] == "null":
            result.pop()
            
        return "[" + ", ".join(result) + "]"

    solution = Solution()
    
    # Test Case 1: A completely unbalanced, right-heavy tree (looks like a linked list)
    # 1 -> 2 -> 3 -> 4
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.right = TreeNode(3)
    root1.right.right.right = TreeNode(4)
    
    print(f"Test 1 Original: {print_level_order(root1)}")
    
    # Run our balancing algorithm
    balanced_root1 = solution.balanceBST(root1)
    
    # Because we pick the middle, 2 or 3 will become the new root.
    print(f"Test 1 Balanced: {print_level_order(balanced_root1)}")
    # Expected output will be a balanced structure like [2, 1, 3, null, null, null, 4] 
    
    # Test Case 2: Already balanced tree
    #      2
    #     / \
    #    1   3
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    
    print(f"\nTest 2 Original: {print_level_order(root2)}")
    balanced_root2 = solution.balanceBST(root2)
    print(f"Test 2 Balanced: {print_level_order(balanced_root2)}")