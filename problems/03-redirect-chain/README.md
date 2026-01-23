# UACS Workshop Problem 03 — Redirect Chain (Chasing Links)

## Background
UACS has a bunch of links posted everywhere (Discord, posters, QR codes).
Some links redirect to other links, and sometimes people accidentally create loops.

You are given a list of redirects between pages numbered 1 to N.
Starting from a given page, repeatedly follow the redirect.

Your job is to determine:
- where you end up if the chain terminates, **or**
- whether you get stuck in a loop.

---

## Input
- The first line contains an integer **N** — the number of pages.
- The next **N** lines each contain an integer **next[i]**:
  - `next[i] = 0` means page `i` has no redirect (the chain stops)
  - otherwise, `next[i]` is the page you are redirected to (1 ≤ next[i] ≤ N)
- The next line contains an integer **S** — the starting page.

---

## Output
Print exactly one line:

- If the redirect chain stops (reaches a page with redirect 0), output:
  ```
  STOP X
  ```
  where `X` is the page where it stops.

- If the chain enters a loop, output:
  ```
  LOOP X
  ```
  where `X` is the first page that is visited **twice** (the first repeated page).

---

## Constraints
- 1 ≤ N ≤ 200000
- 0 ≤ next[i] ≤ N
- 1 ≤ S ≤ N

Your solution should run in **O(N)** time.

---

## Example 1 (stops)

### Input
```
5
2
3
0
5
0
1
```

### Output
```
STOP 3
```

### Explanation
Start at 1: 1 → 2 → 3 → stop (since next[3] = 0)

---

## Example 2 (loop)

### Input
```
6
2
3
4
2
6
0
1
```

### Output
```
LOOP 2
```

### Explanation
Start at 1: 1 → 2 → 3 → 4 → 2 → ...  
The first page visited twice is 2.

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
- Reading command-line arguments and file input
- Following pointer/redirect chains
- Detecting loops using a visited structure
- Writing efficient O(N) solutions
