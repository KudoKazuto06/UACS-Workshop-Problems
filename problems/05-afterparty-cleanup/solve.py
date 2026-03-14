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
    Prints the odd part of each number.
    """

    t = int(f.readline())

    for _ in range(t):
        n = int(f.readline())

        # TODO:
        # Repeatedly divide n by 2 while it is even.
        # When n becomes odd, print it.

        print(n)


def main():
    f = get_input_file()
    solve(f)


if __name__ == "__main__":
    main()