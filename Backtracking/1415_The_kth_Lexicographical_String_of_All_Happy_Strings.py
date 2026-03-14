# Problem: 1415. The k-th Lexicographical String of All Happy Strings of Length n
# Difficulty: Medium
# Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description

# Time Complexity: O(N) - We mathematically determine each character in a single pass without generating other strings.
# Space Complexity: O(N) - We store exactly 'N' characters to build our final string.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # A happy string of length n has exactly 3 * 2^(n-1) possible combinations
        # If k is larger than the total possible combinations, it doesn't exist
        total_happy_strings = 3 * (1 << (n - 1))
        if k > total_happy_strings:
            return ""
            
        # We convert k to a 0-based index to make the modulo math perfectly align
        k -= 1
        ans = []
        choices = ['a', 'b', 'c']
        
        # We build the string character by character
        for i in range(n):
            if i == 0:
                # For the first character, the tree splits into 3 massive branches ('a', 'b', 'c')
                # Each branch holds 2^(n-1) strings
                branch_size = 1 << (n - 1)
                
                # We divide our target 'k' by the branch size to see which of the 3 branches we belong in
                char_index = k // branch_size
                ans.append(choices[char_index])
                
                # We update 'k' to be the remaining steps INSIDE that specific branch
                k %= branch_size
            else:
                # For all subsequent characters, we only have 2 valid choices (since we can't repeat the last char)
                # Each of these 2 sub-branches holds 2^(n - 1 - i) strings
                branch_size = 1 << (n - 1 - i)
                
                # We find the 2 valid letters we are allowed to use
                valid_choices = [c for c in choices if c != ans[-1]]
                
                # We find which of the 2 sub-branches our target 'k' falls into
                char_index = k // branch_size
                ans.append(valid_choices[char_index])
                
                # We update 'k' for the next loop
                k %= branch_size
                
        return "".join(ans)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n = 1, k = 3 -> ["a", "b", "c"]
    print(f"Test 1: {sol.getHappyString(1, 3)}") # Expected: "c"
    
    # Test 2: Out of bounds
    print(f"Test 2: {sol.getHappyString(1, 4)}") # Expected: ""
    
    # Test 3: n = 3, k = 9
    print(f"Test 3: {sol.getHappyString(3, 9)}") # Expected: "cab"