import os
import sys


def main():
    x = list(range(12, 2, -1))
    # don't use slices for this
    # print(x[::-1])
    # I'm confident you can figure it out
    print(f"x reversed = {x}")

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
