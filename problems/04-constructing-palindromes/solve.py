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
    Determines whether the string can be rearranged into a palindrome.
    """

    s = f.readline().strip()

    # TODO:
    # Count how many times each character appears.
    #
    # A string can form a palindrome if
    # at most ONE character has an odd frequency.
    #
    # If more than one character has an odd count,
    # print "IMPOSSIBLE".
    #
    # Otherwise, print "POSSIBLE".

    pass


def main():
    f = get_input_file()
    solve(f)


if __name__ == "__main__":
    main()