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

# Set 2 dimension list
def dim2input(N):
    li = []
    for _ in range(N):
        li.append(list(map(int, input())))
    return li

# --------------------------------------------

dp = None

def main():
    N, Z, W = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if N == 1:
        print(abs(A[0] - W))
    else:
        print(max(
            abs(A[-1] - W),
            abs(A[-1] - A[-2])
        ))

main()
