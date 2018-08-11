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
    N, M = li_input()
    A = li_input()

    ans = 0
    d = collections.defaultdict(lambda: 0)

    cumsum = [0]
    c_sum = 0
    for a in A:
        c_sum = (c_sum + a) % M
        cumsum.append(c_sum)

    for c in cumsum:
        d[c] += 1

    for v in d.values():
        if v >= 2:
            ans += v * (v - 1) // 2

    print(ans)


main()
