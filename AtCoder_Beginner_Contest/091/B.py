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
    B = [input() for _ in range(N)]
    M = int(input())
    R = [input() for _ in range(M)]

    ans = -9999999999999

    for b in B:
        cnt = 0

        for bb in B:
            if b == bb:
                cnt += 1

        for r in R:
            if r == b:
                cnt -= 1

        ans = max(cnt, ans)

    print(max(ans, 0))


main()
