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
    S = input()
    K = int(input())

    A = []
    for i in range(len(S)):
        for j in range(i+1, min(i+6, len(S)+1)):
            A.append(S[i:j])

    print(sorted(list(set(A)))[K-1])

main()
