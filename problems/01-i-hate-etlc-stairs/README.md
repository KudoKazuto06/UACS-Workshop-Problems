# UACS Morning Problem 01 — I Hate ETLC Stairs

## Background
While organizing UACS events, you spend the entire day running between
different buildings and floors on campus (ETLC, CAB, DICE, etc.).

You don’t mind going down — elevators exist.
But going **upstairs** is exhausting.

Given the sequence of floors you visit throughout the day,
calculate how many floors you climbed **upward** in total.

---

## Input
The input consists of:
- One integer **N** — the number of floor visits.
- Followed by **N** lines, each containing an integer **Fᵢ**,
  representing the floor number visited in order.

Floors may be negative (basement levels).

---

## Output
Output a single integer: the **total number of floors climbed upward**.

Only count increases in floor number.
Descending or staying on the same floor does **not** count.

---

## Formal Definition
Compute:

```
total = Σ_{i=2..N} max(0, F_i - F_{i-1})
```

---

## Constraints
- 2 ≤ N ≤ 200000
- −20 ≤ Fᵢ ≤ 200
- Your solution should run in **O(N)** time.

---

## Example

### Input
```
6
2
2
5
3
10
7
```

### Output
```
10
```

### Explanation
- 2 → 2 : +0  
- 2 → 5 : +3  
- 5 → 3 : +0  
- 3 → 10 : +7  
- 10 → 7 : +0  

Total = 3 + 7 = 10

---

## Running the Program

Your program **must support both** of the following:

### Option 1 — Input from a file (recommended)
```bash
python solve.py input.txt
```

### Option 2 — Standard input
```bash
python solve.py < input.txt
```

If a filename is provided as a command-line argument,
read input from that file.
Otherwise, read from standard input.

---

## What You Are Practicing
- Reading input from files and command-line arguments
- Looping through sequences
- Writing efficient O(N) solutions
- Running programs from the command line

This problem is inspired by CMPUT-style “morning problems” and reflects how real programs are tested.
