import sys
import math
import collections
import itertools
import array
import inspect
import bisect

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
    N, M, Q = li_input()
    L, R = [], []
    LL = []

    LR = [li_input() for _ in range(M)]
    LR.sort(key=lambda x: x[1])

    LL_ = [0] * (N + 1)
    for l, r in LR:
        L.append(l)
        R.append(r)
        LL_[l] += 1
        LL.append(LL_[:])

    Query = [li_input() for _ in range(Q)]

    for i in range(len(LL)):
        for j in range(1, len(LL[i])):
            LL[i][j] += LL[i][j - 1]

    for p, q in Query:
        r_idx = bisect.bisect_right(R, q)
        targetLL = LL[r_idx - 1]
        print(targetLL[q])


main()
