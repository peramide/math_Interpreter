import pytest

from interpreter import calculate

def main():
    test_calculate()


def test_calculate():
    assert(calculate(2, "+", 2)) == 4.0
    assert(calculate(2, "-", 1)) == 1.0
    assert(calculate(2, "*", 1)) == 2.0
    assert(calculate(2, "/", 1)) == 2.0


if __name__ == "__main__":
    main()