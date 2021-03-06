import os
import sys

"""
Notes:
- Excellent work! You not only captured the ZeroDivisionError
but you also handled a ValueError
- Good variable names in line with the domain (math). Keep in mind
we always want to remember the domain because it will be easy for
users in that domain to understand the variable names without effort.
"""


def main():
    try:
        x = float(input("x = "))
        y = (x ** 3 - 9 * x) / (x ** 2 - 2 * x + 1)
    except ValueError as ve:
        print(f"warning: {ve}; wrong value")
        y = "x0"
    except ZeroDivisionError as zde:
        print(f"Warning: {zde}; the denominator is zero")
        y = "indefinite number"
    print(f"y is {y}")

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
