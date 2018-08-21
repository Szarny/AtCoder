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
    S = [input() for _ in range(2)]
    is_cols = []

    i = 0
    while i < N:
        if S[0][i] == S[1][i]:
            is_cols.append(True)
            i += 1
        else:
            is_cols.append(False)
            i += 2

    if is_cols[0]:
        ans = 3
    else:
        ans = 6

    i = 1
    while i < len(is_cols):
        if is_cols[i] and is_cols[i - 1]:
            ans *= 2
        elif not is_cols[i] and not is_cols[i - 1]:
            ans *= 3
        elif not is_cols[i] and is_cols[i - 1]:
            ans *= 2

        i += 1

    print(ans % 1000000007)


main()
