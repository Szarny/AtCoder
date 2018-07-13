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

    ans = 0

    div = 1
    while div < len(S) - 1:
        front, rear = set(list(S[:div])), set(list(S[div:]))
        kind = len(front & rear)

        ans = max(ans, kind)

        div += 1

    print(ans)

main()
