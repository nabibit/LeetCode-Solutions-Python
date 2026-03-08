# LeetCode Solutions in Python

![Problems Solved](https://img.shields.io/badge/Problems%20Solved-34-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![Daily Commits](https://img.shields.io/badge/Daily%20Commits-Yes-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

A curated collection of LeetCode problems solved in Python, with a focus on **clean code**, **optimal approaches**, and **detailed complexity analysis**. Updated daily as part of my commitment to consistent practice.

## 📊 Complexity Legend

| Notation | Meaning | Example |
|----------|---------|---------|
| O(1) | Constant time | Hash table lookup / Bitwise ops |
| O(log n) | Logarithmic | Binary search / Heap ops |
| O(n) | Linear | Single pass through array |
| O(n + m) | Linear sum | Iterating through two separate inputs |
| O(n log n) | Linearithmic | Efficient sorting (Timsort) |
| O(n²) | Quadratic | Nested loops / All substrings |
| O(R²) | Quadratic (rows) | Pyramid simulation |
| O(C(n, k)) | Combinatorial | Backtracking valid combinations |
| O(n * k) | Multiplicative | Sliding window with string slicing |
| O(2^k) | Exponential | All binary combinations of length k |

## 📁 Repository Structure

LeetCode-Solutions-Python/

├── Arrays/ # Array manipulation & Sliding Window

├── Backtracking/ # Recursive search & Combinations

├── BitManipulation/ # Bitwise operations

├── DynamicProgramming/ # DP & Simulation

├── Strings/             # String processing

├── Trees/               # BST operations & Traversals

└── README.md


## 📚 Solutions by Category

### [Arrays](./Arrays/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1536 | [Minimum Swaps to Arrange a Binary Grid](./Arrays/1536_Minimum_Swaps_to_Arrange_a_Binary_Grid.py) | Medium | Greedy (Pop/Insert Simulation) | O(N²) | O(N) |
| 1582 | [Special Positions in a Binary Matrix](./Arrays/1582_Special_Positions_in_a_Binary_Matrix.py) | Easy | Matrix Precomputation | O(M * N) | O(M + N) |
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
| 3713 | [Longest Balanced Substring I](./Strings/3713_Longest_Balanced_Substring_I.py) | Medium | Brute Force (All Substrings) | O(n²) | O(1) |
| 3714 | [Longest Balanced Substring II](./Strings/3714_Longest_Balanced_Substring_II.py) | Medium | Prefix Difference Map | O(n) | O(n) |

### [Backtracking](./Backtracking/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 401 | [Binary Watch](./Backtracking/0401_Binary_Watch.py) | Easy | Backtracking / Bit Counting | O(C(10, k)) | O(k) |

### [BitManipulation](./BitManipulation/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 190 | [Reverse Bits](./BitManipulation/0190_Reverse_Bits.py) | Easy | Divide & Conquer (Bitwise Merge) | O(1) | O(1) |
| 693 | [Binary Number with Alternating Bits](./BitManipulation/0693_Binary_Number_with_Alternating_Bits.py) | Easy | Bit Manipulation (XOR & Check) | O(1) | O(1) |
| 762 | [Prime Number of Set Bits in Binary Representation](./BitManipulation/0762_Prime_Number_of_Set_Bits_in_Binary_Representation.py) | Easy | Bit Manipulation + Fast Prime Set | O(n) | O(1) |
| 868 | [Binary Gap](./BitManipulation/0868_Binary_Gap.py) | Easy | Bitwise Shift & Masking | O(log n) | O(1) |
| 1356 | [Sort Integers by The Number of 1 Bits](./BitManipulation/1356_Sort_Integers_by_The_Number_of_1_Bits.py) | Easy | Custom Sort & Bit Count | O(N log N) | O(1) |
| 1404 | [Number of Steps to Reduce a Number in Binary Representation to One](./BitManipulation/1404_Number_of_Steps_to_Reduce_a_Number_in_Binary_Representation_to_One.py) | Medium | Right-to-Left Carry Tracking | O(N) | O(1) |
| 1680 | [Concatenation of Consecutive Binary Numbers](./BitManipulation/1680_Concatenation_of_Consecutive_Binary_Numbers.py) | Medium | Bitwise Shift & Modulo | O(N) | O(1) |
| 3666 | [Minimum Operations to Equalize Binary String](./BitManipulation/3666_Minimum_Operations_to_Equalize_Binary_String.py) | Hard | SortedList BFS Parity Search | O(N log N) | O(N) |

### [DynamicProgramming](./DynamicProgramming/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 799 | [Champagne Tower](./DynamicProgramming/0799_Champagne_Tower.py) | Medium | Simulation + DP (In-place) | O(R²) | O(R) |

### [Trees](./Trees/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1022 | [Sum of Root To Leaf Binary Numbers](./Trees/1022_Sum_of_Root_To_Leaf_Binary_Numbers.py) | Easy | DFS & Bitwise Shift | O(N) | O(H) |
| 1382 | [Balance a Binary Search Tree](./Trees/1382_Balance_a_Binary_Search_Tree.py) | Medium | In-Order Traversal + Divide & Conquer | O(n) | O(n) |

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
Total Problems: 34 

Easy: 15 

Medium: 14 

Hard: 5  

Last updated: Daily  

---

# 💡 Algorithm Technique Map

| Core Category              | Problems |
|----------------------------|----------|
| Greedy / Sorting           | 1536, 1689, 3010, 3634 |
| Sliding Window             | 1461,c1888, 3013 |
| Bit Manipulation           | 67, 190, 401, 693, 762, 868, 1356, 1404, 1680, 3666 |
| DFS / Trees                | 1022, 1382 |
| Dynamic Programming        | 799, 3640 |
| Prefix / Range Queries     | 3714, 3721 |
| Simulation / Linear Scan   | 696, 1582, 1758, 1784, 1980, 3379, 3637 |
| Brute Force / Recursion    | 761, 1545, 3713, 3719 |

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

### Complex Logic

**3013. Divide Array... Min Cost II**: A Hard problem tackled using a Dual Heap (Min/Max) approach to maintain a sliding window of the smallest k elements efficiently.  

**3640. Trionic Array II**: Uses a state machine approach to track multiple DP states (ascent, descent, final ascent) simultaneously, optimizing for scenarios with negative numbers.  

**761. Special Binary String**: A beautiful algorithmic trick that treats special binary strings exactly like valid parentheses. Uses recursion to peel back the "brackets", sort the inner independent blocks, and glue them back together for the lexicographically largest result.

**3721. Longest Balanced Subarray II**: A serious step up from Version I. Uses a Segment Tree with lazy propagation and prefix sums to efficiently manage and query huge array ranges in O(n log n) time.

**3666. Minimum Operations to Equalize Binary String**: A Biweekly Contest Hard problem. Bypasses strict Time Limit Exceeded (TLE) errors in a BFS state-space search by utilizing a `SortedList` and tracking zero-count parities, dropping the lookup time to $O(\log N)$.

**1545. Find Kth Bit in Nth Binary String**: Avoids generating a massive, million-character binary string by treating the sequence generation as a mirror. Uses $O(N)$ recursive Divide & Conquer to mathematically track the position through mirrored and inverted halves.

**1888. Minimum Number of Flips to Make the Binary String Alternating**: Solves a complex cyclic-shift problem using a Sliding Window. Instead of physically reallocating memory to shift characters or doubling the string (`s + s`), it achieves $O(1)$ auxiliary space by using modulo arithmetic (`i % n`) to create a "virtual" doubled string.

**1980. Find Unique Binary String**: Showcases a brilliant implementation of Cantor's Diagonalization argument. Instead of generating and searching through a massive O(2^N) state space, it constructs a guaranteed unique string in strict O(N) time by simply flipping the i-th bit of the i-th string, mathematically proving uniqueness without a single collision check.

### Tree Operations
**1382. Balance a Binary Search Tree**: Demonstrates a brilliant two-step approach to restructuring trees. Instead of complex pointer rotations, it harvests nodes via an O(n) In-Order Traversal to get a sorted array, then uses Divide-and-Conquer to mathematically rebuild a perfectly balanced BST from the middle out.

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