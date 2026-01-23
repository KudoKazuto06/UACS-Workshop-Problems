# Workshop Problem 05 — Afterparty Cleanup (Odd Part)

## Background
After a long day of events, UACS hosts an afterparty 🎉.

Each group of attendees is packed into boxes. However, due to safety rules:
- Boxes can only be split evenly in half **while the group size is even**.
- Once a group size becomes **odd**, it can no longer be split.

The final remaining group size is called the **odd part**.

---

## Problem
For each group size `n`, repeatedly divide it by 2 **while it is even**.
When it becomes odd, output the remaining value.

Formally, every positive integer `n` can be written as:

```
n = (2^k) × m
```

where `m` is odd.  
Your task is to output `m`.

---

## Input
- The first line contains an integer **T** — the number of test cases.
- The next **T** lines each contain one integer **n**, representing a group size.

---

## Output
For each test case, output one line containing the **odd part** of `n`.

---

## Constraints
- 1 ≤ T ≤ 200000
- 1 ≤ n ≤ 10^18

Your solution should be efficient.

---

## Example

### Input
```
5
1
2
12
40
999
```

### Output
```
1
1
3
5
999
```

---

## Explanation
- 1 is already odd → odd part is 1  
- 2 → 2 ÷ 2 = 1  
- 12 → 12 ÷ 2 ÷ 2 = 3  
- 40 → 40 ÷ 2 ÷ 2 ÷ 2 = 5  
- 999 is already odd

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
- Efficient looping and conditionals
- Understanding number properties (odd/even, powers of 2)
- Writing fast solutions for large inputs
