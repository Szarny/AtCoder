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

def sum_of_digit(k):
    k_str = str(k)
    _sum = 0

    for k_letter in k_str:
        _sum += int(k_letter)

    return _sum

def main():
    k = int(input())

    tmp_min = 10**10
    for multiplier in range(1, 100000):
        tmp_min = min(sum_of_digit(k * multiplier), tmp_min)

    print(tmp_min)

main()
