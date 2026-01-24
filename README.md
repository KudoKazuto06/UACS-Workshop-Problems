# UACS Workshop Problems
Designed and hosted by **Cong Thinh Nguyen (Tommy)** for UACS workshops.

A collection of **CMPUT-style programming problems** used in UACS workshops.

This repository contains **5 carefully selected problems** designed to help students practice:
- Writing clean problem-solving code
- Reading input from **files and command-line arguments**
- Running programs from the **command line**
- Understanding how real programs are tested (non-interactive I/O)

The problems are suitable for **high school students and early undergraduates** and mirror the structure used in CMPUT courses.

---

## Repository Structure

```
UACS-Workshop-Problems/
  problems/
    01-problem-name/
      README.md      # Problem description
      solve.py       # Starter code / solution scaffold
      tests/         # Sample input/output files (added later)
    02-problem-name/
    03-problem-name/
    04-problem-name/
    05-problem-name/
```

Each problem is self-contained in its own folder.

---

## How the Problems Work

For each problem:
- You will write your solution inside `solve.py`
- Your program must read input from:
  - a file passed as a command-line argument, **or**
  - standard input (stdin)

### Example usage
```bash
python solve.py input.txt
```

or
```bash
python solve.py < input.txt
```

This reflects how programs are tested in real university courses.

---

## Coding Style Expectations

- Use clear and readable code
- Follow the structure provided in `solve.py`
- Avoid unnecessary complexity
- Focus on correctness and efficiency

The goal is **problem-solving**, not clever tricks.

---

## Who This Is For

- UACS workshop participants
- High school students interested in Computing Science
- Students preparing for CMPUT-style courses
- Anyone learning command-line based programming

---

## Notes

- Bash scripts and automated testing tools may be added later.
- Problems increase gradually in difficulty.
- Input/output formats are strict — follow the problem descriptions carefully.

---

Happy coding 🚀  
University of Alberta Computing Society (UACS)
