# Problem: 67.Add Binary
# Difficulty: Easy
# Link: https://leetcode.com/problems/add-binary/description/

# Time Complexity: O(N + M) - We iterate through the bits (implictly via XOR/AND)
# Space Complexity: O(max(N, M)) - We store the result string 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        # This stores the data as raw bits, which is more memory efficient than converting 
        # than a list of strings characters like ['1', '0', '1', ...]
        x, y = int(a, 2), int(b, 2)

        # We simulate the hardware adder circuit
        # This loop runs until there are no carries left
        while y:
            # XOR (^) calculates the sum WITHOUT carry
            # 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 0 = 0
            answer = x ^ y

            # AND (&) calculates the carry (where both bits are 1)
            # Shift left (<<) moves the carry to the correct position for the next iteration
            carry = (x & y) << 1

            # We update x to be the partial sum, and y to be the new carry
            x, y = answer, carry

        # We convert the final integer back to a binary string
        # slice [2:] removes the "0b" prefix
        return bin(x)[2:]
    
# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11", "1"))     # Expected: "100"
    print(solution.addBinary("1010", "1011")) # Expected: "10101"