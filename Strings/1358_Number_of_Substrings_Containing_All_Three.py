# Problem: 1358. Number of Substrings Containing All Three Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

# Time Complexity: O(N) - We iterate through the string of length N exactly once. 
# Space Complexity: O(1) - We only store three integer variables to track the last seen indices.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track the most recent index where we saw each character
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_valid_substrings = 0
        
        for i, char in enumerate(s):
            # Update the latest position of the current character
            last_seen[char] = i
            
            # If we haven't seen all three characters yet, the minimum will be -1
            # If we have seen all three, the minimum tells us the oldest character's position
            # Every starting index from 0 up to this minimum creates a valid substring
            oldest_index = min(last_seen['a'], last_seen['b'], last_seen['c'])
            
            # Adding 1 accounts for the 0-indexed nature of the string
            if oldest_index != -1:
                total_valid_substrings += oldest_index + 1
                
        return total_valid_substrings

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard mix
    print(f"Test 1: {sol.numberOfSubstrings('abcabc')}") 
    # Expected: 10
    
    # Test 2: Repeating characters at the start
    print(f"Test 2: {sol.numberOfSubstrings('aaacb')}") 
    # Expected: 3 (The valid substrings are 'aaacb', 'aacb', and 'acb')
    
    # Test 3: Missing a character entirely
    print(f"Test 3: {sol.numberOfSubstrings('abc')}") 
    # Expected: 1 (Only the full string works)