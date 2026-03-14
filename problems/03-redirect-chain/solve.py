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
    Follows the redirect chain and determines whether it stops or loops.
    """

    # Read number of pages
    n = int(f.readline())

    # Read redirects, using 1-based indexing
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        nxt[i] = int(f.readline())

    # Read starting page
    s = int(f.readline())

    # TODO:
    # Follow the redirect chain starting from page s.
    #
    # Keep track of which pages have already been visited.
    #
    # At each step:
    #   - if the current page has already been visited,
    #     print "LOOP X" where X is the current page, then stop
    #   - otherwise, mark it as visited
    #   - if nxt[current] == 0,
    #     print "STOP X" where X is the current page, then stop
    #   - otherwise, move to the next page

    pass


def main():
    f = get_input_file()
    solve(f)


if __name__ == "__main__":
    main()