# Problem: 212. Word Search II
# Difficulty: Hard
# Link: https://leetcode.com/problems/word-search-ii/description

# Time Complexity: O(M * N * 3^L) - Where M*N is the board size, and L is the maximum length of a word. We explore at most 3 directions (excluding the cell we came from). The Trie aggressively prunes this.
# Space Complexity: O(W) - Where W is the total number of characters in the dictionary words to build the Trie, plus O(L) for the recursion stack.

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word if this node is the end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word  # Mark the end of the word
            
        ROWS, COLS = len(board), len(board[0])
        res = []
        
        # DFS Traversal tightly coupled with the Trie
        def dfs(r, c, node):
            # Read the character and check if it's in our Trie
            char = board[r][c]
            if char not in node.children:
                return
            
            # Step down the Trie
            next_node = node.children[char]
            
            # Did we find a word?
            if next_node.word:
                res.append(next_node.word)
                # Optimization: Prevent finding the same word twice and prune the Trie
                next_node.word = None
                
            # Temporarily mark the cell as visited to prevent revisiting in the current path
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
                    
            # Backtrack: Restore the cell for other DFS paths
            board[r][c] = char
            
            # Optimization: If this Trie node has no more valid children (all words found),
            # prune it to prevent future dead-end traversals!
            if not next_node.children:
                del node.children[char]

        # Initiate DFS from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return res

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Search
    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    print(f"Test 1: {sol.findWords(board1, words1)}") 
    # Expected: ["oath","eat"]
    
    # Test 2: Impossible Search
    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    print(f"Test 2: {sol.findWords(board2, words2)}") 
    # Expected: []