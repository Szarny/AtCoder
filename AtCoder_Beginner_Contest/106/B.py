import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(10000)


# Debug output
def chkprint(*args):
    names = {
        id(v): k
        for k, v in inspect.currentframe().f_back.f_locals.items()
    }
    print(', '.join(
        names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args))


# Binary converter
def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]


# --------------------------------------------

dp = None


def main():
    N = int(input())
    L = [105, 135, 165, 189, 195]

    if N < 105:
        print(0)
    elif N < 135:
        print(1)
    elif N < 165:
        print(2)
    elif N < 189:
        print(3)
    elif N < 195:
        print(4)
    else:
        print(5)


main()
