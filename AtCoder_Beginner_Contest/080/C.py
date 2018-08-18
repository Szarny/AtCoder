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
    F = [li_input() for _ in range(N)]
    P = [li_input() for _ in range(N)]

    ans = (-1) * (10**100)

    for i in range(1, 1024):
        B = to_bin(i)

        tmpans = 0
        for j in range(len(F)):
            match = 0
            for other, joisino in zip(F[j], B):
                if other == int(joisino) == 1:
                    match += 1

            tmpans += P[j][match]

        ans = max(ans, tmpans)

    print(ans)


main()
