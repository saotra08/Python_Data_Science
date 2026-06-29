import sys
import string


def count(text):
    """Count and print the number of every characters categories in the text"""
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(c.isupper() for c in text)} upper letters")
    print(f"{sum(c.islower() for c in text)} lower letters")
    print(f"{sum(c in string.punctuation for c in text)} punctuation marks")
    print(f"{sum(c.isspace() for c in text)} spaces")
    print(f"{sum(c.isdigit() for c in text)} digits")


def main():
    """Get the text argument and count every characters categories"""
    try:
        args = sys.argv[1:]
        assert len(args) <= 1, "more than one argument is provided"
        if len(args) == 0:
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = args[0]
        count(text)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
