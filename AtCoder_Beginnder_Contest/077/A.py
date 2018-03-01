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
        li.append(input().split())
    return li

# --------------------------------------------

dp = None

def main():
    C = []
    C.append(input())
    C.append(input())

    cond1 = C[0][0] == C[1][2]
    cond2 = C[0][1] == C[1][1]
    cond3 = C[0][2] == C[1][0]

    if cond1 and cond2 and cond3:
        print("YES")
    else:
        print("NO")

main()
