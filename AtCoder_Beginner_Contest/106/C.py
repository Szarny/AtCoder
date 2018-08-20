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
    S = input()
    K = int(input())

    if S == 1:
        print(S[0])
        return

    if K == 1:
        print(S[0])
        return

    i = 0
    while True:
        if S[i] != "1":
            print(S[i])
            return

        if i == K - 1:
            print(1)
            return

        i += 1


main()
