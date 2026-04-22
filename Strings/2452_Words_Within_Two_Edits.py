# Problem: 2452. Words Within Two Edits of Dictionary
# Difficulty: Medium
# Link: https://leetcode.com/problems/words-within-two-edits-of-dictionary/description

# Time Complexity: O(Q * D * L) - Where Q is the number of queriee, D is the number of dictionary words, and L is the length of the words. (Early exits drastically reduce real-world time)
from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        valid_queries = []

        for query in queries:
            for dict_word in dictionary:
                differences = 0

                # Compare letters at the exact same positions
                for q_char, d_char in zip(query, dict_word):
                    if q_char != d_char:
                        differences += 1
                    
                    # Early exit: If we exceed 2 edits, this dictionary is a lost cause
                    if differences > 2:
                        break
                
                # If we finished the word with 2 or fewer differences, it's a valid match
                if differences <= 2:
                    valid_queries.append(query)
                    break # Early exit: We found a match, no need to check the rest of the dictionary


        return valid_queries
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard matching
    print(f"Test 1: {sol.twoEditWords(['word','note','ants','wood'], ['wood','joke','moat'])}") 
    # Expected: ['word', 'note', 'wood']
    # ('word' -> 'wood' in 1 edit. 'note' -> 'joke' in 2 edits. 'ants' -> fails. 'wood' -> 'wood' in 0 edits.)
    
    # Test 2: No matches possible
    print(f"Test 2: {sol.twoEditWords(['yes'], ['not'])}") 
    # Expected: []