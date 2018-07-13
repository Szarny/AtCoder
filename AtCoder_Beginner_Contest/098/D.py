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

def xor(A):
    ret = 0
    for a in A:
        ret ^= a
    return ret

def main():
    N = int(input())
    A = [int(_) for _ in input().split()]

    l, r = 0, 0

    ans = 0
    while l <= N - 1:
        csum = sum(A[l:r + 1])
        cxor = xor(A[l:r + 1])

        print(l, r, csum, cxor)

        if l == r:
            ans += 1
            r += 1
        else:
            if r != N and csum == cxor:
                ans += 1
                r += 1
            else:
                l += 1

    print(ans)

main()
