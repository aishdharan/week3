import os
import sys
import random

"""
Notes:
- Excellent attempt
"""


def main():
    x = random.choices(range(5), k=20)
    x0 = x.count(0)
    x1 = x.count(1)
    x2 = x.count(2)
    x3 = x.count(3)
    x4 = x.count(4)
    print(f'x = {x}')
    print(f'no. of zeroes = {x0}, no. of ones = {x1}, no. of twos = {x2}, no. of threes = {x3}, no. of fours = {x4}')

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
