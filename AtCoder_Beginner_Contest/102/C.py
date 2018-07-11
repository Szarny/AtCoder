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
    N = int(input())
    A = [int(_) for _ in input().split()]

    i = 0
    while i < len(A):
        A[i] -= (i + 1)
        i += 1

    A.sort()
    b = A[len(A) // 2]

    sad = 0
    for a in A:
        sad += abs(a - b)

    print(sad)

main()
