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
    a, b = [int(_) for _ in input().split()]
    diff = b - a

    tower = 0
    ts = []
    for add in range(1, 1000):
        tower += add
        ts.append(tower)

    print(ts[diff-2] - a)

main()
