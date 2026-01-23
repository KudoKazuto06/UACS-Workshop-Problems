import sys


def get_input_file():
    """
    Returns a file object to read input from.
    If a filename is provided as a command-line argument,
    read from that file. Otherwise, read from standard input.
    """
    if len(sys.argv) > 1:
        return open(sys.argv[1], "r")
    return sys.stdin


def solve(f):
    """
    Computes the total number of floors climbed upward.
    """

    # Read number of floor visits
    n = int(f.readline())

    # Read the first visited floor
    prev = int(f.readline())

    # total_up represents the total number of floors climbed upward
    total_up = 0

    # TODO:
    # Read the remaining (n - 1) floor numbers, one per line.
    # For each new floor:
    #   - compare it with the previous floor
    #   - if the new floor is higher, add the difference to total_up
    #   - update the previous floor
    #
    # Use a loop to process the input efficiently.

    # Output the final result
    print(total_up)


def main():
    f = get_input_file()
    solve(f)


if __name__ == "__main__":
    main()
