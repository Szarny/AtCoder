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
    N, C = [int(_) for _ in input().split()]
    nr0, nr1, nr2 = 0, 0, 0

    Diff = []
    for _ in range(C):
        Diff.append([int(__) for __ in input().split()])

    Color = []
    for _ in range(N):
        Color.append([int(__) for __ in input().split()])

    R0 = collections.defaultdict(lambda: 0)
    R1 = collections.defaultdict(lambda: 0)
    R2 = collections.defaultdict(lambda: 0)

    for y in range(N):
        for x in range(N):
            r = (y + x) % 3

            if r == 0:
                R0[Color[y][x]] += 1
                nr0 += 1
            elif r == 1:
                R1[Color[y][x]] += 1
                nr1 += 1
            else:
                R2[Color[y][x]] += 1
                nr2 += 1

    R0s = []
    for dist_color in range(C):
        d = 0
        for src_color in R0.keys():
            d += Diff[src_color-1][dist_color] * R0[src_color]

        R0s.append(d)

    R1s = []
    for dist_color in range(C):
        d = 0
        for src_color in R1.keys():
            d += Diff[src_color-1][dist_color] * R1[src_color]

        R1s.append(d)

    R2s = []
    for dist_color in range(C):
        d = 0
        for src_color in R2.keys():
            d += Diff[src_color-1][dist_color] * R2[src_color]

        R2s.append(d)
        
    ans = 10**100
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or i == k:
                    continue

                ans = min(ans, R0s[i] + R1s[j] + R2s[k])

    print(ans)

main()
