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
    N = input()
    op = ["+", "-"]

    for op1 in op:
        for op2 in op:
            for op3 in op:
                if eval(N[0] + op1 + N[1] + op2 + N[2] + op3 + N[3]) == 7:
                    print(N[0] + op1 + N[1] + op2 + N[2] + op3 + N[3] + "=7")
                    return

main()
