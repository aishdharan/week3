import os
import sys


def main():
    # they don't have to be ints only
    A11 = float(input("A11 = "))
    A12 = float(input("A12 = "))
    A13 = float(input("A13 = "))
    A14 = float(input("A14 = "))
    A15 = float(input("A15 = "))
    A16 = float(input("A16 = "))
    A17 = float(input("A17 = "))
    A18 = float(input("A18 = "))
    A19 = float(input("A19 = "))
    B11 = float(input("B11 = "))
    B12 = float(input("B12 = "))
    B13 = float(input("B13 = "))
    B14 = float(input("B14 = "))
    B15 = float(input("B15 = "))
    B16 = float(input("B16 = "))
    B17 = float(input("B17 = "))
    B18 = float(input("B18 = "))
    B19 = float(input("B19 = "))

    A = [
        [A11, A12, A13],
        [A14, A15, A16],
        [A17, A18, A19]
    ]
    print(f'A = {A}')
    B = [
        [B11, B12, B13],
        [B14, B15, B16],
        [B17, B18, B19]
    ]
    print(f'B = {B}')
    C11 = A11 * B11 + A12 * B14 + A13 * B17
    C12 = A11 * B12 + A12 * B15 + A13 * B18
    C13 = A11 * B13 + A12 * B16 + A13 * B19
    C14 = A14 * B11 + A15 * B14 + A16 * B17
    C15 = A14 * B12 + A15 * B15 + A16 * B18
    C16 = A14 * B13 + A15 * B16 + A16 * B19
    C17 = A17 * B11 + A18 * B14 + A19 * B17
    C18 = A17 * B12 + A18 * B15 + A19 * B18
    C19 = A17 * B13 + A18 * B16 + A19 * B19
    # nice Python formatting
    C = [
        [C11, C12, C13],
        [C14, C15, C16],
        [C17, C18, C19]
    ]
    # since we asked for A** and B** we can report A * B
    print(f"matrix multiplication of 3x3 with 3x3 is A * B = {C}")

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
