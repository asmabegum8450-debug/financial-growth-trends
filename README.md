# Interview Prep: Analyzing Financial Growth Trends (Array)

## Problem Description

In this problem, we are given a sorted array of integers representing yearly financial growth percentages.
These values may include **negative numbers**, **zero**, and **positive numbers**.

Negative numbers represent a decrease in revenue.

The goal is to **return a new array containing the squared values of the growth percentages, sorted in non-decreasing order.**

### Example

Input:

[-5, -2, 0, 3, 10]

Output:

[0, 4, 9, 25, 100]

Explanation:

After squaring the numbers:

[25, 4, 0, 9, 100]

After sorting:

[0, 4, 9, 25, 100]

---

# Clarifying Questions

Before solving the problem, it is important to ask a few clarifying questions:

1. Is the input array always sorted in non-decreasing order?
2. Can the input array be empty?
3. Can the array contain duplicate values?
4. Can the values be negative, zero, and positive?
5. Should the function return a new array or modify the original one?

For this solution we assume:

* The input array **is sorted**
* The function **returns a new array**
* The array **may contain negative values**

---

# Brute Force Approach

A simple solution is:

1. Square every element in the array
2. Sort the resulting array

Example idea:

square each number
sort the array

### Time Complexity

O(n log n)

Because sorting takes O(n log n).

### Space Complexity

O(n)

Because we create a new array.

---

# Optimized Approach (Two Pointer Technique)

Since the input array is already sorted, we can improve the solution.

Observation:

The largest squared value will come from the number with the **largest absolute value**.

The largest absolute values are located either:

* at the **start** of the array (large negative numbers)
* at the **end** of the array (large positive numbers)

So we use **two pointers**.

---

# Steps of the Algorithm

1. Create a result array with the same size as the input.
2. Place one pointer at the **beginning** of the array.
3. Place one pointer at the **end** of the array.
4. Compare the **absolute values** of both numbers.
5. Square the larger value.
6. Insert it into the result array starting from the **end**.
7. Move the corresponding pointer.
8. Repeat until all elements are processed.

This ensures the result array stays sorted.

---

# Algorithm Flow (Flowchart)

Start
↓
Initialize left pointer and right pointer
↓
Compare absolute values
↓
Square the larger value
↓
Insert into result array
↓
Move pointer
↓
Repeat until done
↓
Return result array

---

# Test Cases

## Normal Cases

Input: [-5, -2, 0, 3, 10]
Output: [0, 4, 9, 25, 100]

Input: [-8, -3, 2, 4, 12]
Output: [4, 9, 16, 64, 144]

Input: [-7, -1, 2, 3, 11]
Output: [1, 4, 9, 49, 121]

---

## Edge Cases

Input: []
Output: []

Input: [0]
Output: [0]

Input: [-3, -2, -1]
Output: [1, 4, 9]

Input: [0, 0, 0]
Output: [0, 0, 0]

---

# Time Complexity

O(n)

The algorithm processes the array **once** using two pointers.

---

# Space Complexity

O(n)

A new array is created to store the squared values.

---

# Running the Program

To run the solution:

python solution.py

Example output:

Input: [-5, -2, 0, 3, 10]
Output: [0, 4, 9, 25, 100]

---

# Running the Tests

To run the unit tests:

python -m unittest test_solution.py

Example output:

Ran 6 tests

OK

This confirms the solution works for **normal cases and edge cases**.

---

# Repository Structure

financial-growth-trends/

solution.py
test_solution.py
README.md
flowchart.png

---

# Video Demonstration

The video includes:

* Problem explanation
* Clarifying questions
* Explanation of brute force approach
* Optimized two-pointer solution
* Code walkthrough
* Running the program in the terminal
* Running unit tests
* Time and space complexity explanation
