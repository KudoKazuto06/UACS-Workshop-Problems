#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    echo "Usage: bash tools/run_one.sh <problem_number>"
    echo "Example: bash tools/run_one.sh 1"
    exit 1
fi

if command -v python >/dev/null 2>&1; then
    PY_CMD="python"
elif command -v python3 >/dev/null 2>&1; then
    PY_CMD="python3"
elif command -v py >/dev/null 2>&1; then
    PY_CMD="py"
else
    echo "Error: no Python interpreter found."
    echo "Make sure one of these works: python, python3, or py"
    exit 1
fi

PROBLEM_NUM=$(printf "%02d" "$1")
PROBLEM_DIR=$(ls -d problems/${PROBLEM_NUM}-* 2>/dev/null)

if [ -z "$PROBLEM_DIR" ]; then
    echo "Problem $1 not found."
    exit 1
fi

TEST_DIR="$PROBLEM_DIR/tests"
PROGRAM="$PROBLEM_DIR/solve.py"

if [ ! -f "$PROGRAM" ]; then
    echo "Missing solve.py in $PROBLEM_DIR"
    exit 1
fi

TOTAL=0
PASSED=0

echo "Running tests for problem $1"
echo "Using: $PY_CMD"
echo

for infile in "$TEST_DIR"/*.in; do
    [ -e "$infile" ] || continue

    base=$(basename "$infile" .in)
    outfile="$TEST_DIR/$base.out"

    TOTAL=$((TOTAL + 1))

    result=$($PY_CMD "$PROGRAM" "$infile")
    expected=$(tr -d '\r' < "$outfile")

    result=$(printf "%s" "$result" | tr -d '\r')

    if [ "$result" = "$expected" ]; then
        echo "[PASS] $base"
        PASSED=$((PASSED + 1))
    else
        echo "[FAIL] $base"
        echo "Expected: $expected"
        echo "Got: $result"
        echo
    fi
done

echo "---------------------"
echo "Passed $PASSED / $TOTAL tests"

if [ "$TOTAL" -gt 0 ]; then
    PERCENT=$((PASSED * 100 / TOTAL))
else
    PERCENT=0
fi

echo "Pass rate: $PERCENT%"