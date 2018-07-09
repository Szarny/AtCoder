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
    names = {id(v):k for k,v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

# Binary converter
def to_bin(x):
    return bin(x)[2:]

# --------------------------------------------

dp = None

def main():
    D, N = [int(_) for _ in input().split()]

    if D == 0:
        if N != 100:
            print(N)
        else:
            print(101)

    elif D == 1:
        if N != 100:
            print(100 * N)
        else:
            print(10100)

    else:
        if N != 100:
            print(10000 * N)
        else:
            print(1010000)

main()
