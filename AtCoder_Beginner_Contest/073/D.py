import sys
import math
import collections
import itertools
import array
import inspect
import pprint

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
        li.append(input().split())
    return li

# --------------------------------------------

dp = None

def main():
    N, M, R = list(map(int, input().split()))
    Rs = list(map(int, input().split()))

    Mx = []
    for _ in range(N+1):
        Mx.append([-1] * (N+1))

    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        Mx[a][b] = c
        Mx[b][a] = c

    pprint.pprint(Mx)

main()
