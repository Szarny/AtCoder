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

M = None

def f(C):
    return abs(sum(C[0][:M])) + abs(sum(C[1][:M])) + abs(sum(C[2][:M]))

def main():
    global M

    N, M = [int(_) for _ in input().split()]

    C = []
    for _ in range(N):
        x, y, z = [int(__) for __ in input().split()]
        C.append([x, y, z])

    if M == 0:
        print(0)
        sys.exit()

    V = [[] for _ in range(8)]

    for c in C:
        V[0].append(c[0] + c[1] + c[2])
        V[1].append(c[0] + c[1] - c[2])
        V[2].append(c[0] - c[1] + c[2])
        V[3].append(c[0] - c[1] - c[2])
        V[4].append(- c[0] + c[1] + c[2])
        V[5].append(- c[0] + c[1] - c[2])
        V[6].append(- c[0] - c[1] + c[2])
        V[7].append(-c[0] - c[1] - c[2])

    ans = -1
    for v in V:
        v.sort(reverse=True)
        ans = max(ans, abs(sum(v[:M])))

    print(ans)

main()
