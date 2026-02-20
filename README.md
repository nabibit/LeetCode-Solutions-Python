# LeetCode Solutions in Python

![Problems Solved](https://img.shields.io/badge/Problems%20Solved-17-blue)
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

## 📁 Repository Structure

LeetCode-Solutions-Python/

├── Arrays/ # Array manipulation & Sliding Window

├── Backtracking/ # Recursive search & Combinations

├── BitManipulation/ # Bitwise operations

├── DynamicProgramming/ # DP & Simulation

├── Strings/ # String processing

└── README.md


## 📚 Solutions by Category

### [Arrays](./Arrays/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
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

### [DynamicProgramming](./DynamicProgramming/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 799 | [Champagne Tower](./DynamicProgramming/0799_Champagne_Tower.py) | Medium | Simulation + DP (In-place) | O(R²) | O(R) |

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
Total Problems: 16 

Easy: 8 

Medium: 5  

Hard: 4  

Last updated: Daily  

---

## 💡 Key Algorithms Used

| Technique                              | Problem Numbers        |
|----------------------------------------|------------------------|
| Greedy + Sorting                      | 3010                   |
| Sliding Window + Two Heaps            | 3013                   |
| Two Pointers + Sorting                | 3634                   |
| Simulation / Modular Arithmetic       | 3379                   |
| Linear Scan / Pattern Recognition     | 3637, 696                   |
| Dynamic Programming / State Machine   | 799, 3640              |
| Brute Force (All Subarrays/Substrings)| 3713, 3719             |
| Prefix Sum / Difference Map           | 3714                   |
| Bit Manipulation                      | 67, 190, 693           |
| Backtracking / Bit Counting           | 401                    |
| Recursion + String Sorting             | 761
| Segment Tree / Lazy Propagation        | 3721                   |

## 📝 Solution Highlights

### Efficient Implementations

**67. Add Binary**: Simulates a hardware adder using XOR and AND operations, handling carry-overs efficiently.  

**696. Count Binary Substrings**: Uses a single pass to group consecutive identical characters, then sums the minimum of adjacent group lengths - an O(n) time, O(1) space solution.

**3714. Longest Balanced Substring II**: Optimizes a string problem from O(n²) to O(n) by tracking prefix differences in a hash map.  

**401. Binary Watch**: Uses backtracking with pruning to explore only valid time combinations, avoiding unnecessary checks.  

**693. Binary Number with Alternating Bits**: Uses a clever bitwise trick: XOR the number with its right shift; if the result is all ones, the bits alternate. Then checks if (x & (x + 1)) == 0 to confirm all bits are set.

**Brute Force Approaches 3713. Longest Balanced Substring I & 3719. Longest Balanced Subarray I**: Both demonstrate straightforward brute‑force solutions by checking all substrings/subarrays. While not optimal, they serve as clear baselines and illustrate the problem constraints.

### Complex Logic

**3013. Divide Array... Min Cost II**: A Hard problem tackled using a Dual Heap (Min/Max) approach to maintain a sliding window of the smallest k elements efficiently.  

**3640. Trionic Array II**: Uses a state machine approach to track multiple DP states (ascent, descent, final ascent) simultaneously, optimizing for scenarios with negative numbers.  

**761. Special Binary String**: A beautiful algorithmic trick that treats special binary strings exactly like valid parentheses. Uses recursion to peel back the "brackets", sort the inner independent blocks, and glue them back together for the lexicographically largest result.

**3721. Longest Balanced Subarray II**: A serious step up from Version I. Uses a Segment Tree with lazy propagation and prefix sums to efficiently manage and query huge array ranges in O(n log n) time.

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LeetCode-Solutions-Python.git
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