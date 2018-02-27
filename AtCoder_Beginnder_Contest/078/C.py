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
    n_case, n_tle = list(map(int, input().split()))

    t_each_submit = 1900 * n_tle + 100 * (n_case - n_tle)

    mean_submit_times = (2 ** n_tle)

    print(t_each_submit * mean_submit_times)

main()
