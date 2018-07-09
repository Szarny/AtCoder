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

""" input template
S = input()
N = int(input())
L = list(map(int, input().split()))
a, b = list(map(int, input().split()))
SL = list(input())
"""

# --------------------------------------------

dp = None

def main():
    pass

main()
