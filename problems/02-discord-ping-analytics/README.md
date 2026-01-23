# UACS Workshop Problem 02 — Discord Ping Analytics

## Background
UACS runs events and announcements, and your Discord server gets **a lot** of pings.

During a day, you record how many pings happen each minute. Then, you want to quickly answer questions like:

> “How many pings happened from minute L to minute R?”

You must answer many such queries efficiently.

---

## Input
- The first line contains an integer **N** — the number of minutes recorded.
- The second line contains **N** integers `a1 a2 ... aN` where `ai` is the number of pings in minute `i`.
- The third line contains an integer **Q** — the number of queries.
- The next **Q** lines each contain two integers **L R** (1-indexed), asking for the total number of pings from minute **L** to minute **R**, inclusive.

---

## Output
For each query, output one integer on its own line: the sum of `aL + a(L+1) + ... + aR`.

---

## Constraints
- 1 ≤ N ≤ 200000
- 0 ≤ ai ≤ 10^6
- 1 ≤ Q ≤ 200000
- 1 ≤ L ≤ R ≤ N

Your solution should run fast. A direct loop for every query may be too slow.

---

## Example

### Input
```
8
2 0 3 1 4 0 2 5
4
1 3
4 4
3 7
2 8
```

### Output
```
5
1
10
15
```

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
- Efficient query answering (preprocessing)
- Careful indexing (1-indexed queries)
- Writing clean, structured code in `solve(f)`
