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
    x = int(input())

    A = [1]
    for a in range(2, 100):
        for b in range(2, 10000):
            if a ** b <= 1000:
                A.append(a ** b)
            else:
                break

    print(sorted(filter(lambda a: a<=x, A))[-1])



main()
