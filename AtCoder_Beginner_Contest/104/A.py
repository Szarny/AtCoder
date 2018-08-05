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
    R = int(input())

    if R < 1200:
        print("ABC")
    elif R < 2800:
        print("ARC")
    else:
        print("AGC")


main()
