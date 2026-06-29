import sys
from ft_filter import ft_filter


def main():
    """rogram that accepts two arguments: a string (S) and an integer (N),
    program that output a list of words from S that have a length greater
    than N."""
    try:
        args = sys.argv[1:]
        assert len(args) == 2, "the arguments are bad"
        text, n = args
        assert not text.isdigit(), "the arguments are bad"
        assert n.isdigit(), "the arguments are bad"
        n = int(n)
        words = [word for word in text.split(" ")]
        print(ft_filter(lambda word: len(word) > n, words))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
