#!/usr/bin/env bash

if command -v python >/dev/null 2>&1; then
    PY_CMD="python"
elif command -v python3 >/dev/null 2>&1; then
    PY_CMD="python3"
elif command -v py >/dev/null 2>&1; then
    PY_CMD="py"
else
    echo "Error: no Python interpreter found."
    exit 1
fi

echo "UACS Workshop Judge"
echo "===================="
echo

for dir in problems/*/; do

    PROBLEM_DIR="${dir%/}"
    NAME=$(basename "$PROBLEM_DIR")
    TEST_DIR="$PROBLEM_DIR/tests"
    PROGRAM="$PROBLEM_DIR/solve.py"

    if [ ! -d "$TEST_DIR" ]; then
        continue
    fi

    if [ ! -f "$PROGRAM" ]; then
        continue
    fi

    echo "Running $NAME"

    TOTAL=0
    PASSED=0

    for infile in "$TEST_DIR"/*.in; do

        base=$(basename "$infile" .in)
        outfile="$TEST_DIR/$base.out"

        TOTAL=$((TOTAL + 1))

        result=$($PY_CMD "$PROGRAM" "$infile")
        expected=$(tr -d '\r' < "$outfile")

        result=$(printf "%s" "$result" | tr -d '\r')

        if [ "$result" = "$expected" ]; then
            PASSED=$((PASSED + 1))
        else
            echo "  [FAIL] $base"
            echo "    Expected: $expected"
            echo "    Got: $result"
        fi
    done

    PERCENT=$((PASSED * 100 / TOTAL))

    echo "  Passed $PASSED / $TOTAL ($PERCENT%)"
    echo
done

echo "Done."