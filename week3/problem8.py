import os
import sys
import random


def main():
    r = int(input("Give a number: "))
    r_rand = random.choices(range(0, 10), k=10)
    print(r_rand)
    print(f"You win? {r in r_rand}")
    try:
        assert 0 <= r < 10
    except AssertionError:
        print(f"error: invalid number {r}. Give a number =>0 and <10")
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
