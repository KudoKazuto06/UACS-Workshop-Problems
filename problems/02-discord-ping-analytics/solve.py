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
    Answers range sum queries efficiently.
    """

    # Read number of minutes recorded
    n = int(f.readline())

    # Read ping counts for each minute
    arr = list(map(int, f.readline().split()))

    # TODO:
    # Build a prefix sum array where prefix[i] stores
    # the total number of pings from minute 1 to minute i.
    #
    # One common approach is:
    # prefix[0] = 0
    # prefix[1] = arr[0]
    # prefix[2] = arr[0] + arr[1]
    # ...
    #
    # This allows each query [L, R] to be answered in O(1):
    # answer = prefix[R] - prefix[L - 1]

    # Read number of queries
    q = int(f.readline())

    # TODO:
    # For each query:
    #   - read L and R
    #   - compute the sum from L to R using prefix sums
    #   - print the result

    pass


def main():
    f = get_input_file()
    solve(f)


if __name__ == "__main__":
    main()