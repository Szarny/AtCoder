import sys
import math
import collections
import itertools
import array
import inspect
import copy

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
        li.append(input().split())
    return li

# --------------------------------------------

dp = None

def calc_rect_area(P):
    left = 10**10
    right = -(10**10)
    upper = -(10**10)
    lower = 10**10

    for p in P:
        left = min(p[0], left)
        right = max(p[0], right)
        upper = max(p[1], upper)
        lower = min(p[1], lower)

    area = (right - left) * (upper - lower)

    return area

def main():
    N, K = list(map(int, input().split()))
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))

    P_original = copy.deepcopy(P)

    # Y座標->X座標の順に点をソートする
    P.sort(key=lambda x:x[1])
    P.sort(key=lambda x:x[0])

    idx = 0
    limit = len(P) - K
    min_area = 10**100
    while idx <= limit:
        min_area = min(
            calc_rect_area(P[idx:idx+K]),
            min_area
        )
        idx += 1

    P = P_original

    P.sort(key=lambda x:x[0])
    P.sort(key=lambda x:x[1])

    idx = 0
    while idx <= limit:
        min_area = min(
            calc_rect_area(P[idx:idx+K]),
            min_area
        )
        idx += 1

    print(min_area)

main()
