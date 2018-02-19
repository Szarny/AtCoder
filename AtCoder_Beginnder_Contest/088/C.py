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
    C = []

    for _ in range(3):
        C.append(list(map(int, input().split())))

    a1_limit = min(C[0])+1
    a2_limit = min(C[1])+1
    a3_limit = min(C[2])+1
    b1_limit = min(C[0][0], C[1][0], C[2][0])+1
    b2_limit = min(C[0][1], C[1][1], C[2][1])+1
    b3_limit = min(C[0][2], C[1][2], C[2][2])+1

    A1, A2, A3, B1, B2, B3 = [], [], [], [], [], []
    for i in range(a1_limit):
        A1.append(i)
    for i in range(a2_limit):
        A2.append(i)
    for i in range(a3_limit):
        A3.append(i)
    for i in range(b1_limit):
        B1.append(i)
    for i in range(b2_limit):
        B2.append(i)
    for i in range(b3_limit):
        B3.append(i)

    for a1, a2, a3 in itertools.product(A1, A2, A3):
        b1 = C[0][0] - a1
        b2 = C[1][1] - a2
        b3 = C[2][2] - a3

        if a1 + b1 != C[0][0]:
            continue
        if a2 + b1 != C[1][0]:
            continue
        if a3 + b1 != C[2][0]:
            continue
        if a1 + b2 != C[0][1]:
            continue
        if a2 + b2 != C[1][1]:
            continue
        if a3 + b2 != C[2][1]:
            continue
        if a1 + b3 != C[0][2]:
            continue
        if a2 + b3 != C[1][2]:
            continue
        if a3 + b3 != C[2][2]:
            continue

        print("Yes")
        return

    print("No")

main()
