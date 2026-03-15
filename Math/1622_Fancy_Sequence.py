# Problem: 1622. Fancy Sequence
# Difficulty: Hard
# Link: https://leetcode.com/problems/fancy-sequence/description

# Time Complexity: 
#   - append(): O(log MOD) due to the modular inverse calculation using Fermat's Little Theorem.
#   - addAll(), multAll(), getIndex(): O(1) pure constant time math.
# Space Complexity: O(N) - We store the anti-scaled values in a single array.

class Fancy:
    def __init__(self):
        self.seq = []
        # We track the global operations applied to the entire array
        # Think of this as the equation: y = x * mul + add
        self.add = 0
        self.mul = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # We need to store a "shrunk" value (x) so that: x * mul + add = val
        # Solving for x: x = (val - add) / mul
        # In modular arithmetic, division by 'mul' is multiplication by the modular inverse of 'mul'
        
        # We calculate the modular inverse using Fermat's Little Theorem: pow(mul, MOD - 2, MOD)
        mod_inverse = pow(self.mul, self.MOD - 2, self.MOD)
        
        # Apply the anti-math before saving it to the array
        stored_val = ((val - self.add) * mod_inverse) % self.MOD
        self.seq.append(stored_val)

    def addAll(self, inc: int) -> None:
        # Adding to the sequence just increases our global adder.
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        # Multiplying the sequence scales BOTH the global multiplier and the global adder!
        # Because (x * mul + add) * m = x * (mul * m) + (add * m)
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        # If the index doesn't exist, return -1
        if idx >= len(self.seq):
            return -1
            
        # We take the raw, "shrunk" value from our array and apply the current global math to it
        ans = (self.seq[idx] * self.mul + self.add) % self.MOD
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    fancy = Fancy()
    fancy.append(2)       # seq = [2]
    fancy.addAll(3)       # seq = [5]
    fancy.append(7)       # seq = [5, 7]
    fancy.multAll(2)      # seq = [10, 14]
    
    print(f"Index 0: {fancy.getIndex(0)}") # Expected: 10
    
    fancy.addAll(3)       # seq = [13, 17]
    fancy.append(10)      # seq = [13, 17, 10]
    fancy.multAll(2)      # seq = [26, 34, 20]
    
    print(f"Index 0: {fancy.getIndex(0)}") # Expected: 26
    print(f"Index 1: {fancy.getIndex(1)}") # Expected: 34
    print(f"Index 2: {fancy.getIndex(2)}") # Expected: 20