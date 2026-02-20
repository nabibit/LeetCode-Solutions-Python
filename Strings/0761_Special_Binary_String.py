# Problem: 761. Special Binary String
# Difficulty: Hard
# Link: https://leetcode.com/problems/special-binary-string/description

# Time Complexity: O(N^2) is the worst case (e.g., "111...000") where we recurse deeply without splitting much),
#                   but generally much faster on average due to string splitting.
# Space Complexity: O(N) - The recursion stack and the creation of substrings take linear space relative to the string length.
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base Case: if the string is empty return it
        if not s:
            return ""

        block = []
        balance = 0
        start = 0

        # We iterate through the string to find top-level irreductible special strings
        for i, char in enumerate(s):
            balance += 1 if char == '1' else -1

            # When balance is 0, we've found a complete special substring
            if balance == 0:
                # We strip the outer '1' and '0' and recursively process the inner substring
                inner_processed = self.makeLargestSpecial(s[start + 1: i])

                # We reconstruct the block and add it to our list
                block.append('1' + inner_processed + '0')

                # We move the start pointer to the beginning of the next potential block
                start = i + 1

        # We sort the blocks in descending order to maximize the lexicographical value
        block.sort(reverse=True)

        # We concatenate and return the sorted blocks
        return "".join(block)
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: "11011000"
    # The string splits into "11011000" -> outer '1' and '0', inner "101100".
    # Inner "101100" splits into "10" and "1100".
    # We sort them: "1100" comes before "10", so it becomes "110010".
    # We wrap it back: "1" + "110010" + "0" = "11100100".
    print(f"Test 1: {solution.makeLargestSpecial('11011000')}") # Expected: "11100100"
    
    # Test Case 2: "10"
    # Smallest irreducible special string. Returns "10".
    print(f"Test 2: {solution.makeLargestSpecial('10')}") # Expected: "10"