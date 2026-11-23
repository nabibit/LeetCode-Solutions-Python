# Problem: 1352. Product of the Last K Numbers
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-the-last-k-numbers/

# Time Complexity: O(1) for both add() and getProduct() - Just list appends and single integer division.
# Space Complexity: O(N) - Stores the running prefix products since the last zero was seen.

class ProductOfNumbers:

    def __init__(self):
        # Start with a dummy 1 so our division math works cleanly on the very first element
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # A zero wipes out any previous product that includes it,
            # so just reset the array and start fresh from here
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches past our current prefix array, it means a 0 happened within the last k numbers
        if k >= len(self.prefix):
            return 0
        
        # Otherwise, divide the total running product by the product right before our k-window
        return self.prefix[-1] // self.prefix[-1 - k]


# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    pon = ProductOfNumbers()
    pon.add(3)        # [3]
    pon.add(0)        # [3, 0] -> resets prefix
    pon.add(2)        # [3, 0, 2]
    pon.add(5)        # [3, 0, 2, 5]
    pon.add(4)        # [3, 0, 2, 5, 4]
    
    print(f"Last 2: {pon.getProduct(2)}") # Expected: 20 (5 * 4)
    print(f"Last 3: {pon.getProduct(3)}") # Expected: 40 (2 * 5 * 4)
    print(f"Last 4: {pon.getProduct(4)}") # Expected: 0  (crosses the 0)
    
    pon.add(8)        # [3, 0, 2, 5, 4, 8]
    print(f"Last 2: {pon.getProduct(2)}") # Expected: 32 (4 * 8)