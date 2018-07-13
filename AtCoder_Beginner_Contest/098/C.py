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
    S = input()

    ans = S[1:].count("E")
    A = []
    A.append(ans)

    for i in range(1, N):
        if S[i - 1] == "W":
            ans += 1
        if S[i] == "E":
            ans -= 1
        A.append(ans)

    print(min(A))



main()
