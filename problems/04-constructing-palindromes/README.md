# Workshop Problem 04 — Constructing Palindromes

## Problem
A palindrome is a string that reads the same forwards and backwards (for example, `racecar` and `abba`).

You are given a string `s` consisting of lowercase English letters. Your task is to construct **any** palindrome using **all** characters of `s` exactly once.

If it is impossible to form a palindrome, print `IMPOSSIBLE`.

---

## Input
- One line containing a string `s` (only lowercase letters `a`–`z`).

---

## Output
- If a palindrome can be formed, output one valid palindrome using all characters of `s`.
- Otherwise, output:
  ```
  IMPOSSIBLE
  ```

If multiple palindromes are possible, you may output **any** one.

---

## Constraints
- 1 ≤ |s| ≤ 200000
- `s` contains only lowercase English letters

Your solution should run in **O(|s|)** time (or close).

---

## Example 1

### Input
```
aabb
```

### Output
```
abba
```

(Other correct outputs include `baab`.)

---

## Example 2

### Input
```
abc
```

### Output
```
IMPOSSIBLE
```

---

## Explanation
A string can be rearranged into a palindrome if and only if:
- at most **one** character occurs an odd number of times.

---

## Running the Program

Your program must support both of the following:

### Option 1 — Input from a file (recommended)
```bash
python solve.py input.txt
```

### Option 2 — Standard input
```bash
python solve.py < input.txt
```

If a filename is provided as a command-line argument, read input from that file.
Otherwise, read from standard input.

---

## What You Are Practicing
- Counting frequencies of characters
- Reasoning about necessary/sufficient conditions
- Constructing a valid output (not just computing a number)
- Writing efficient solutions for large input sizes
