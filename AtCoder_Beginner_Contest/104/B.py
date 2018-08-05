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
    names = {id(v): k for k, v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))

# Binary converter


def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]

# --------------------------------------------


dp = None


def main():
    lower = "abcdefghijklmnopqrstuvwxyzAC"
    S = input()

    if S[0] != "A":
        print("WA")
        return

    if S[2:-1].count("C") != 1:
        print("WA")
        return

    for s in S:
        if s not in lower:
            print("WA")
            return

    print("AC")


main()
