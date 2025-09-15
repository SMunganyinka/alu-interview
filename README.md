# ALU Interview - Coding Challenges

This repository contains solutions for multiple coding challenges.

## Projects

### 1. Minimum Operations

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

#### Requirements
- Prototype: `def minOperations(n)`
- Returns an integer.
- If `n` is impossible to achieve or `n <= 1`, return `0`.

#### Example
For `n = 9`:
`H` => `Copy All` => `Paste` => `HH` (2 ops)
`HH` => `Paste` => `HHH` (3 ops total)
`HHH` => `Copy All` => `Paste` => `HHHHHH` (5 ops total)
`HHHHHH` => `Paste` => `HHHHHHHHH` (6 ops total)
Result: 6 operations.

#### Approach
The problem can be solved by finding the sum of the prime factors of `n`.
If we have `k` characters and want to achieve `k * f` characters (where `f` is a factor):
1. `Copy All`: 1 operation (clipboard now holds `k` characters).
2. `Paste` (`f-1` times): `f-1` operations.
This step takes a total of `1 + (f-1) = f` operations to multiply the current character count by `f`.
Thus, to get `n` characters starting from 1, if `n = p1 * p2 * ... * pk` (prime factorization), the total minimum operations will be `p1 + p2 + ... + pk`.

### 2. Rain Water Trapping

Given a list of non-negative integers representing the heights of walls with unit width 1, calculate how many square units of water will be retained after it rains.

#### Requirements
- Prototype: `def rain(walls)`
- `walls` is a list of non-negative integers
- Returns an integer indicating total amount of rainwater retained
- Assume that the ends of the list are not walls and will not retain water
- If the list is empty, return 0

#### Example
For `walls = [0, 1, 0, 2, 0, 3, 0, 4]`:
```
     |
 |   |
 | | |
 | | |
_| |_|_
```
Result: 6 units of water trapped.

#### Approach
The solution uses a two-pointer approach:
1. Start with pointers at both ends of the array
2. Keep track of the maximum height seen so far from left and right
3. Move the pointer with the smaller height inward
4. If current height is less than the max height from that side, water can be trapped

### File Structure
- `minimum_operations/`: Directory containing the minimum operations solution
  - `0-minoperations.py`: Python script with the `minOperations` function
  - `0-main.py`: Main file for testing
- `rain/`: Directory containing the rain water trapping solution
  - `0-rain.py`: Python script with the `rain` function
  - `0_main.py`: Main file for testing

### Usage
To test the solutions:

#### Minimum Operations
```bash
cd minimum_operations
python 0-main.py
```

#### Rain Water Trapping
```bash
cd rain
python 0_main.py
```

### Constraints
- Python 3.4.3
- PEP 8 style
- All files start with `#!/usr/bin/python3`
- All files end with a newline
- All files must be executable 
