# LeetCode Solutions in Python

![Problems Solved](https://img.shields.io/badge/Problems%20Solved-56-green)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![Daily Commits](https://img.shields.io/badge/Daily%20Commits-Yes-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

A curated collection of LeetCode problems solved in Python, with a focus on **clean code**, **optimal approaches**, and **detailed complexity analysis**. Updated daily as part of my commitment to consistent practice.

## 📊 Complexity Legend

| Notation | Meaning | Example |
|----------|---------|---------|
| O(1) | Constant | Hash table lookup / Bitwise ops / Math |
| O(log n) | Logarithmic | Binary search / Single Heap ops |
| O(n) | Linear | Single pass through array/string |
| O(n + m) | Linear Sum | Iterating through two separate inputs |
| O(max(n, m)) | Max Linear | Processing the longer of two inputs |
| O(n log n) | Linearithmic | Efficient sorting / Segment Trees |
| O(n²) | Quadratic | Nested loops / All substrings |
| O(n * m) | Multiplicative | 2D Grid traversal / State-space DP (e.g., O(Z * O)) |
| O(V + E) | Graph Linear | DFS/BFS traversing Vertices and Edges |
| O(E log M) | Graph Logarithmic | Kruskal's Algorithm / Binary Search on Edges |
| O(C(n, k)) | Combinatorial | Backtracking valid combinations |
| O(2^k) | Exponential | All binary combinations of length k |
| O(H) | Tree Height | Space complexity for recursive Call Stack |
| O(U) | Unique Elements | Space complexity for Hash Sets |


## 📁 Repository Structure

LeetCode-Solutions-Python/

├── Arrays/              # 1D Array manipulation & Sliding Window

├── Backtracking/        # Recursive search & Combinations

├── BinarySearch/        # Search space optimization & Math

├── BitManipulation/     # Bitwise operations

├── DynamicProgramming/  # DP & Simulation

├── Graphs/              # DSU, Kruskal's, & Binary Search

├── Math/                # Modular Arithmetic & Number Theory

├── Matrix/              # 2D Grids, Traversals, & Boundary Simulation

├── Strings/             # String processing

├── Trees/               # BST operations & Traversals

└── README.md


## 📚 Solutions by Category

### [Arrays](./Arrays/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1536 | [Minimum Swaps to Arrange a Binary Grid](./Arrays/1536_Minimum_Swaps_to_Arrange_a_Binary_Grid.py) | Medium | Greedy (Pop/Insert Simulation) | O(N²) | O(N) |
| 1582 | [Special Positions in a Binary Matrix](./Arrays/1582_Special_Positions_in_a_Binary_Matrix.py) | Easy | Matrix Precomputation | O(M * N) | O(M + N) |
| 1878 | [Get Biggest Three Rhombus Sums in a Grid](./Arrays/1878_Get_Biggest_Three_Rhombus_Sums.py) | Medium | Boundary Simulation | O(M*N*min(M,N)) | O(U) |
| 3010 | [Divide an Array Into Subarrays With Minimum Cost I](./Arrays/3010_Divide_an_Array_Into_Subbarrays_With_Minimum_Cost_I.py) | Easy | Greedy + Sorting | O(n log n) | O(n) |
| 3013 | [Divide an Array Into Subarrays With Minimum Cost II](./Arrays/3013_Divide_an_Array_Into_Subbarrays_With_Minimum_Cost_II.py) | Hard | Sliding Window + Two Heaps | O(n log d) | O(n) |
| 3379 | [Transformed Array](./Arrays/3379_Transformed_Array.py) | Easy | Simulation (Modular Arithmetic) | O(n) | O(n) |
| 3634 | [Minimum Removals to Balance Array](./Arrays/3634_Minimum_Removals_to_Balance.py) | Medium | Two Pointers + Sorting | O(n log n) | O(1) |
| 3637 | [Trionic Array I](./Arrays/3637_Trionic_Array_I.py) | Easy | Linear Scan (Pattern Recognition) | O(n) | O(1) |
| 3640 | [Trionic Array II](./Arrays/3640_Trionic_Array_II.py) | Hard | Dynamic Programming (State Machine) | O(n) | O(n) |
| 3719 | [Longest Balanced Subarray I](./Arrays/3719_Longest_Balanced_Subarray_I.py) | Medium | Brute Force (All Subarrays)| O(n²) | O(n) |
| 3721 | [Longest Balanced Subarray II](./Arrays/3721_Longest_Balanced_Subarray_II.py) | Hard | Segment Tree + Prefix Sums | O(n log n) | O(n) |

### [Strings](./Strings/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 67 | [Add Binary](./Strings/0067_Add_Binary.py) | Easy | Bit Manipulation (Simulation) | O(n + m) | O(max(n,m)) |
| 696 | [Count Binary Substrings](./Strings/0696_Count_Binary_Substrings.py) | Easy | Linear Scan (Group Counting) | O(n) |	O(1) |
| 761 | [Special Binary String](./Strings/0761_Special_Binary_String.py) | Hard | Recursion + Sorting | O(n²) | O(n) |
| 1461 | [Check If a String Contains All Binary Codes](./Strings/1461_Check_If_String_Contains_All_Binary_Codes.py) | Medium | Sliding Window Set / Rolling Hash | O(N) | O(N*K) |
| 1545 | [Find Kth Bit in Nth Binary String](./Strings/1545_Find_Kth_Bit_in_Nth_Binary_String.py) | Medium | Divide & Conquer (Recursion) | O(N) | O(N) |
| 1689 | [Partitioning Into Minimum Number Of Deci-Binary Numbers](./Strings/1689_Partitioning_into_Minimum_number_Of_Deci-Binary_Numbers.py) | Medium | Greedy (Max Digit Search) | O(n) | O(1) |
| 1758 | [Minimum Changes To Make Alternating Binary String](./Strings/1758_Minimum_Changes_To_Make_Alternating_Binary_String.py) | Easy | Symmetric Pattern Counting | O(n) | O(1) |
| 1784 | [Check if Binary String Has at Most One Segment of Ones](./Strings/1784_Check_if_Binary_String_Has_at_Most_One_Segment_of_Ones.py) | Easy | Linear Scan State Tracking | O(n) | O(1) |
| 1888 | [Minimum Number of Flips to Make the Binary String Alternating](./Strings/1888_Minimum_Number_of_Flips_to_Make_the_Binary_String_Alternating.py) | Medium | Sliding Window (Virtual Doubling) | O(N) | O(1) |
| 1980 | [Find Unique Binary String](./Strings/1980_Find_Unique_Binary_String.py) | Medium | Cantor's Diagonalization | O(N) | O(N) |
| 2839 | [Check if Strings Can be Made Equal With Operations I](./Strings/2839_Check_if_Strings_Can_be_Made_Equal.py) | Easy | Parity Grouping + Sorting | O(1) | O(1) |
| 2840 | [Check if Strings Can be Made Equal With Operations II](./Strings/2840_Check_if_Strings_Can_be_Made_Equal_II.py) | Medium | Parity Grouping + Frequency Map | O(N) | O(1) |
| 3713 | [Longest Balanced Substring I](./Strings/3713_Longest_Balanced_Substring_I.py) | Medium | Brute Force (All Substrings) | O(n²) | O(1) |
| 3714 | [Longest Balanced Substring II](./Strings/3714_Longest_Balanced_Substring_II.py) | Medium | Prefix Difference Map | O(n) | O(n) |

### [Backtracking](./Backtracking/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 401 | [Binary Watch](./Backtracking/0401_Binary_Watch.py) | Easy | Backtracking / Bit Counting | O(C(10, k)) | O(k) |
| 1415 | [The k-th Lexicographical String of All Happy Strings of Length n](./Backtracking/1415_The_kth_Lexicographical_String_of_All_Happy_Strings.py) | Medium | Combinatorial Math / Decision Tree | O(N) | O(N) |

### [BinarySearch](./BinarySearch/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 3296 | [Minimum Number of Seconds to Make Mountain Height Zero](./BinarySearch/3296_Min_Seconds_Mountain_Zero.py) | Medium | Binary Search on Answer + Quadratic Formula | O(N log M) | O(1) |

### [BitManipulation](./BitManipulation/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 190 | [Reverse Bits](./BitManipulation/0190_Reverse_Bits.py) | Easy | Divide & Conquer (Bitwise Merge) | O(1) | O(1) |
| 693 | [Binary Number with Alternating Bits](./BitManipulation/0693_Binary_Number_with_Alternating_Bits.py) | Easy | Bit Manipulation (XOR & Check) | O(1) | O(1) |
| 762 | [Prime Number of Set Bits in Binary Representation](./BitManipulation/0762_Prime_Number_of_Set_Bits_in_Binary_Representation.py) | Easy | Bit Manipulation + Fast Prime Set | O(n) | O(1) |
| 868 | [Binary Gap](./BitManipulation/0868_Binary_Gap.py) | Easy | Bitwise Shift & Masking | O(log n) | O(1) |
| 1009 | [Complement of Base 10 Integer](./BitManipulation/1009_Complement_of_Base_10_Integer.py) | Easy | Bitmask & XOR | O(1) | O(1) |
| 1356 | [Sort Integers by The Number of 1 Bits](./BitManipulation/1356_Sort_Integers_by_The_Number_of_1_Bits.py) | Easy | Custom Sort & Bit Count | O(N log N) | O(1) |
| 1404 | [Number of Steps to Reduce a Number in Binary Representation to One](./BitManipulation/1404_Number_of_Steps_to_Reduce_a_Number_in_Binary_Representation_to_One.py) | Medium | Right-to-Left Carry Tracking | O(N) | O(1) |
| 1680 | [Concatenation of Consecutive Binary Numbers](./BitManipulation/1680_Concatenation_of_Consecutive_Binary_Numbers.py) | Medium | Bitwise Shift & Modulo | O(N) | O(1) |
| 3666 | [Minimum Operations to Equalize Binary String](./BitManipulation/3666_Minimum_Operations_to_Equalize_Binary_String.py) | Hard | SortedList BFS Parity Search | O(N log N) | O(N) |

### [DynamicProgramming](./DynamicProgramming/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 799 | [Champagne Tower](./DynamicProgramming/0799_Champagne_Tower.py) | Medium | Simulation + DP (In-place) | O(R²) | O(R) |
| 1594 | [Maximum Non Negative Product in a Matrix](./DynamicProgramming/1594_Max_Non_Negative_Product_Matrix.py) | Medium | 2D DP (Min/Max Dual-State) | O(M*N) | O(M*N) |
| 2946 | [Matrix Similarity After Cyclic Shifts](./Matrix/2946_Matrix_Similarity_After_Cyclic_Shifts.py) | Easy | Modular Arithmetic + Slice Comparison | O(M*N) | O(N) |
| 3129 | [Find All Possible Stable Binary Arrays I](./DynamicProgramming/3129_Find_All_Possible_Stable_Binary_Arrays_I.py) | Medium | DP with Invalid State Subtraction | O(Z * O) | O(Z * O) |
| 3130 | [Find All Possible Stable Binary Arrays II](./DynamicProgramming/3130_Find_All_Possible_Stable_Binary_Arrays_II.py) | Hard | DP with Invalid State Subtraction | O(Z * O) | O(Z * O) |
| 3418 | [Maximum Amount of Money Robot Can Earn](./DynamicProgramming/3418_Max_Money_Robot_Can_Earn.py) | Medium | 3D DP (State Tracking) | O(M*N) | O(M*N) |

### [Trees](./Trees/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1022 | [Sum of Root To Leaf Binary Numbers](./Trees/1022_Sum_of_Root_To_Leaf_Binary_Numbers.py) | Easy | DFS & Bitwise Shift | O(N) | O(H) |
| 1382 | [Balance a Binary Search Tree](./Trees/1382_Balance_a_Binary_Search_Tree.py) | Medium | In-Order Traversal + Divide & Conquer | O(n) | O(n) |

### [Graphs](./Graphs/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 3600 | [Maximize Spanning Tree Stability with Upgrades](./Graphs/3600._Maximize_Spanning_Tree_Stability_with_Uprades.py) | Hard | Binary Search on Answer + Kruskal's (DSU) | O(E log M) | O(V + E) |

### [Math](./Math/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1622 | [Fancy Sequence](./Math/1622_Fancy_Sequence.py) | Hard | Modular Inverse (Fermat's Little Theorem) | O(1)* | O(N) |

### [Matrix](./Matrix/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1727 | [Largest Submatrix With Rearrangements](./Matrix/1727_Largest_Submatrix_With_Rearrangements.py) | Medium | Histogram Heights + Greedy Sorting | O(M * N log N) | O(1) |
| 1886 | [Determine Whether Matrix Can Be Obtained By Rotation](./Matrix/1886_Determine_Whether_Matrix_Can_Be_Obtained_By_Rotation.py) | Easy | In-Place Transpose + Reverse | O(N²) | O(1) |
| 2906 | [Construct Product Matrix](./Matrix/2906_Construct_Product_Matrix.py) | Medium | Prefix & Suffix Sweeps | O(N*M) | O(1)* |
| 3070 | [Count Submatrices with Top-Left Element and Sum Less Than k](./Matrix/3070_Count_Submatrices_Top_Left.py) | Medium | 2D Prefix Sum + Staircase Pruning | O(M*N) | O(1) |
| 3212 | [Count Submatrices With Equal Frequency of X and Y](./Matrix/3212_Count_Submatrices_Equal_Frequency.py) | Medium | Space-Optimized 2D Prefix Sum | O(M*N) | O(N) |
| 3546 | [Equal Sum Grid Partition I](./Matrix/3546_Equal_Sum_Grid_Partition_I.py) | Medium | 1D Spatial Projection + Prefix Sum | O(M*N) | O(M+N) |
| 3567 | [Minimum Absolute Difference in Sliding Submatrix](./Matrix/3567_Min_Abs_Difference_Sliding_Submatrix.py) | Medium | Submatrix Extraction + Sorting | O(M*N*K²logK) | O(K²) |
| 3548 | [Equal Sum Grid Partition II](./Matrix/3548_Equal_Sum_Grid_Partition_II.py) | Hard | Topological Connectivity + Dynamic Maps | O(M*N) | O(M*N) |
| 3643 | [Flip Square Submatrix Vertically](./Matrix/3643_Flip_Square_Submatrix_Vertically.py) | Easy | Two-Pointer Slice Swap | O(K²) | O(K) |

## 🎯 Problem Solving Approach

Each solution file follows a consistent structure to ensure readability and maintainability:

```python
# Problem: [Problem Name]
# Difficulty: [Difficulty Level]
# Link: [LeetCode Link]

# Time Complexity: O(?) - [Explanation of the dominant operation]
# Space Complexity: O(?) - [Explanation of auxiliary space used]

class Solution:
    def method_name(self, ...):
        # Implementation with clear comments holding the logic
        pass

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    print(solution.method_name(...))
```

## 📈 Progress Tracker
Total Problems: 56 

Easy: 20 

Medium: 27 

Hard: 9  

Last updated: Daily  

---

# 💡 Algorithm Technique Map

| Core Category              | Problems |
|----------------------------|----------|
| Greedy / Sorting           | 1536, 1689, 1727, 3010, 3634 |
| Sliding Window             | 1461, 1888, 3013 |
| Bit Manipulation           | 67, 190, 401, 693, 762, 868, 1009, 1356, 1404, 1680, 3666 |
| DFS / Trees                | 1022, 1382 |
| Dynamic Programming        | 799, 1594, 3129, 3130, 3418, 3640 |
| Prefix / Range Queries     | 2906, 3070, 3212, 3546, 3714, 3721 |
| Simulation / Linear Scan   | 696, 1582, 1758, 1784, 1878, 1980, 3379, 3637 |
| Brute Force / Recursion    | 761, 1545, 3713, 3719 |
| Graphs    | 3600 |
| Binary Search on Answer    | 3600, 3296 |
| Backtracking / Decision Tree | 401, 1415 |
| Math / Modular Arithmetic  | 1622 |
| Matrix / 2D Traversal      | 1582, 1594, 1727, 1878, 1886, 2906, 2946, 3070, 3212, 3546, 3548, 3567, 3643 |
| String Manipulation / Parity | 2839, 2840 |

## 📝 Solution Highlights

### Efficient Implementations

**67. Add Binary**: Simulates a hardware adder using XOR and AND operations, handling carry-overs efficiently.  

**696. Count Binary Substrings**: Uses a single pass to group consecutive identical characters, then sums the minimum of adjacent group lengths - an O(n) time, O(1) space solution.

**3714. Longest Balanced Substring II**: Optimizes a string problem from O(n²) to O(n) by tracking prefix differences in a hash map.  

**401. Binary Watch**: Uses backtracking with pruning to explore only valid time combinations, avoiding unnecessary checks.  

**693. Binary Number with Alternating Bits**: Uses a clever bitwise trick: XOR the number with its right shift; if the result is all ones, the bits alternate. Then checks if (x & (x + 1)) == 0 to confirm all bits are set.

**Brute Force Approaches 3713. Longest Balanced Substring I & 3719. Longest Balanced Subarray I**: Both demonstrate straightforward brute‑force solutions by checking all substrings/subarrays. While not optimal, they serve as clear baselines and illustrate the problem constraints.

**762. Prime Number of Set Bits**: Leverages Python's highly optimized `.bit_count()` method and a hardcoded O(1) lookup set for primes up to 20, avoiding complex math checks on the fly and keeping the solution blazing fast.

**1461. Check If a String Contains All Binary Codes**: Showcases the progression from a standard O(N*K) sliding window Hash Set to a bare-metal O(2^K) Rolling Hash. By using bitwise shifts to update the window and a `bytearray` as a boolean checklist, it reduces a potential 100MB string allocation down to a 1MB footprint.


**1758. Minimum Changes To Make Alternating Binary String**: Avoids simulating both possible alternating string patterns by using mathematical symmetry: if Pattern A requires `x` flips, Pattern B mathematically requires exactly `N - x` flips. 

**1689. Partitioning Into Minimum Number Of Deci-Binary Numbers**: Reduces a seemingly complex dynamic programming problem into a pure $O(N)$ Greedy scan by realizing the number of required deci-binary layers is simply equal to the maximum single digit found within the string.

**3643. Flip Square Submatrix Vertically**: Showcases idiomatic Python by utilizing slice assignment (`grid[top][y:y+k], grid[bottom][y:y+k] = ...`) combined with a two-pointer approach to reverse a targeted submatrix in-place, keeping the codebase extremely clean and avoiding the boilerplate of nested element-wise swapping loops.

**1886. Determine Whether Matrix Can Be Obtained By Rotation**: Avoids complex coordinate mapping by breaking a 90-degree matrix rotation into two primitive $O(1)$ space operations: a diagonal transposition followed by a horizontal row reversal. This allows for rapid, in-place orientation checks without allocating memory for rotated copies.

**2946. Matrix Similarity After Cyclic Shifts**: Bypasses the Time Limit Exceeded (TLE) trap of simulating massive shift constraints by utilizing Modular Arithmetic (`k % n`). To achieve strict $O(1)$ auxiliary space, it abandons array reallocation entirely, instead mapping cyclical coordinate geometry to dynamically verify if an element `k` steps away matches the current index.

### Complex Logic

**3013. Divide Array... Min Cost II**: A Hard problem tackled using a Dual Heap (Min/Max) approach to maintain a sliding window of the smallest k elements efficiently.  

**3640. Trionic Array II**: Uses a state machine approach to track multiple DP states (ascent, descent, final ascent) simultaneously, optimizing for scenarios with negative numbers.  

**761. Special Binary String**: A beautiful algorithmic trick that treats special binary strings exactly like valid parentheses. Uses recursion to peel back the "brackets", sort the inner independent blocks, and glue them back together for the lexicographically largest result.

**3721. Longest Balanced Subarray II**: A serious step up from Version I. Uses a Segment Tree with lazy propagation and prefix sums to efficiently manage and query huge array ranges in O(n log n) time.

**3666. Minimum Operations to Equalize Binary String**: A Biweekly Contest Hard problem. Bypasses strict Time Limit Exceeded (TLE) errors in a BFS state-space search by utilizing a `SortedList` and tracking zero-count parities, dropping the lookup time to $O(\log N)$.

**1545. Find Kth Bit in Nth Binary String**: Avoids generating a massive, million-character binary string by treating the sequence generation as a mirror. Uses $O(N)$ recursive Divide & Conquer to mathematically track the position through mirrored and inverted halves.

**1888. Minimum Number of Flips to Make the Binary String Alternating**: Solves a complex cyclic-shift problem using a Sliding Window. Instead of physically reallocating memory to shift characters or doubling the string (`s + s`), it achieves $O(1)$ auxiliary space by using modulo arithmetic (`i % n`) to create a "virtual" doubled string.

**1980. Find Unique Binary String**: Showcases a brilliant implementation of Cantor's Diagonalization argument. Instead of generating and searching through a massive O(2^N) state space, it constructs a guaranteed unique string in strict O(N) time by simply flipping the i-th bit of the i-th string, mathematically proving uniqueness without a single collision check.

**3129. Find All Possible Stable Binary Arrays I**: Optimizes a complex combinatorial problem down to an $O(Z \times O)$ time complexity using bottom-up Dynamic Programming. Instead of using an inner loop to validate block sizes, it achieves $O(1)$ state transitions by mathematically subtracting the exact number of invalid sequences that just exceeded the consecutive character `limit`.

**1415. The k-th Lexicographical String of All Happy Strings of Length n**: Bypasses the standard $O(2^N)$ backtracking generation by using Combinatorics. It calculates the exact branch of the decision tree the $k$-th string resides in at every character position, effectively predicting the entire path in strict $O(N)$ time.

**3130. Find All Possible Stable Binary Arrays II**: Scales the mathematical state subtraction logic to handle Hard constraints (over 1,000,000 DP states). By decoupling a heavy 3D matrix into two independent 2D arrays (`dp0` and `dp1`), this architectural tweak drastically reduces Python's memory allocation overhead and pointer-chasing latency, allowing the algorithm to comfortably beat strict Time Limit Exceeded (TLE) constraints.

**1622. Fancy Sequence**: Bypasses the need for a heavy Segment Tree with lazy propagation by leveraging Affine Transformations ($y = mx + c$) and Fermat's Little Theorem. Instead of updating $10^5$ array elements on every API call, it modifies the global state in $O(1)$ time, applying a modular inverse to "pre-shrink" newly appended values so they correctly align with future global transformations.

**1727. Largest Submatrix With Rearrangements**: Transforms a chaotic 2D matrix rearrangement problem into a classic histogram area problem. By calculating consecutive vertical 1s in-place and greedily sorting each row's heights, it completely bypasses the need for combinatorial column shuffling, finding the optimal area in $O(M \cdot N \log N)$ time.

**3070. Count Submatrices with Top-Left Element and Sum Less Than k**: Bypasses the strict $O(M \times N)$ execution time by applying a spatial "Staircase Pruning" technique to a 2D Prefix Sum. By realizing that extending a matrix across non-negative integers guarantees a monotonic increase in sum, it aggressively shrinks the column iteration boundaries the moment a sum exceeds $k$, dropping the real-world time complexity closer to $O(\text{Valid Matrices} + M)$.

**3212. Count Submatrices With Equal Frequency of X and Y**: Implements a 2D Prefix Sum without allocating a full $O(M \times N)$ auxiliary matrix or mutating the input data. By tracking a running horizontal row count and cumulatively adding it to a 1D vertical column array, it successfully evaluates all top-left submatrices while minimizing the space complexity to a strict $O(N)$.

**3567. Minimum Absolute Difference in Sliding Submatrix**: Demonstrates constraint-driven algorithm selection. Instead of over-engineering a complex 2D rolling window or utilizing balanced BSTs, it leverages the microscopic grid constraints ($N \le 30$) to deploy an ultra-lean $O(M \cdot N \cdot K^2 \log K)$ brute-force submatrix extraction and sorting mechanism, optimizing for real-world execution speed over theoretical asymptotic bounds.

**1594. Maximum Non Negative Product in a Matrix**: Demonstrates the failure of greedy pathfinding algorithms when dealing with negative multiplication. It uses a 2D Dynamic Programming matrix to track dual-states (`max_product`, `min_product`) at every cell, successfully maintaining the lowest negative bounds to capitalize on sign-flipping operations further down the grid.

**2906. Construct Product Matrix**: Solves a 2D variation of the classic "Product Except Self" problem while navigating strict non-prime modulo constraints ($12345$). Because the modulo is non-prime, division via Modular Multiplicative Inverse is mathematically invalid. This solution elegantly bypasses the need for division entirely by flattening the matrix traversal into an $O(N \cdot M)$ two-pass algorithm, calculating running prefix and suffix products while updating the result matrix in-place for $O(1)$ auxiliary space.

**3546. Equal Sum Grid Partition I**: Bypasses the need for a heavy 2D Prefix Sum matrix by utilizing 1D Spatial Projection. Because valid cuts must span the entire length or width of the grid, the $O(M \times N)$ 2D matrix can be mathematically squashed into two independent 1D arrays (`row_sums` and `col_sums`). This reduces the partitioning logic to a trivial 1D running prefix sum check, drastically simplifying the codebase and boundary conditions.

**3548. Equal Sum Grid Partition II**: Bypasses severe Time Limit Exceeded (TLE) constraints by replacing heavy $O(N^2)$ graph-connectivity validation (BFS/DFS) with absolute topological properties. It leverages the mathematical proof that removing any single internal node from a $\ge 2 \times 2$ grid graph maintains its connected components, strictly limiting boundary-deletion checks to 1D isolated sub-vectors. This reduces the problem back to a highly-optimized $O(M \times N)$ frequency map sweep.

### Tree Operations
**1382. Balance a Binary Search Tree**: Demonstrates a brilliant two-step approach to restructuring trees. Instead of complex pointer rotations, it harvests nodes via an O(n) In-Order Traversal to get a sorted array, then uses Divide-and-Conquer to mathematically rebuild a perfectly balanced BST from the middle out.

### Graph Operations
**3600. Maximize Spanning Tree Stability with Upgrades**: Combines Binary Search on the Answer with Kruskal's Algorithm. Instead of building a complex dynamic tree, it efficiently validates a target "stability" score by constructing a Spanning Tree using a Disjoint Set Union (DSU) and optimally budgeting edge upgrades.

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/bcyberly/LeetCode-Solutions-Python.git
cd LeetCode-Solutions-Python
```
### Run any solution locally
```
python Strings/0067_Add_Binary.py
```

## 🤝 Contributing

While this is my personal learning repository, I welcome:

⭐ Stars if you find it helpful

🐛 Issues for suggesting improvements

💬 Discussions about alternative approaches

## 📅 Daily Commitment

I solve and commit at least one problem daily. Check the commits to see my progress!

### ⭐ Star this repo if you find it useful!
*Happy Coding! 🚀*