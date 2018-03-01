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
        li.append(input().split())
    return li

# --------------------------------------------

dp = None

def main():
    H, W = list(map(int, input().split()))

    S = []
    for _ in range(H):
        S.append(list(input()))

    for idx_h in range(H):
        for idx_w in range(W):
            if S[idx_h][idx_w] == "#":
                continue

            bomb = 0

            for dh in range(-1, 2):
                new_h = idx_h + dh
                for dw in range(-1, 2):
                    new_w = idx_w + dw

                    if dh == 0 and dw == 0:
                        continue

                    if 0 <= new_h < H and 0 <= new_w < W and S[new_h][new_w] == "#":
                        bomb += 1

            S[idx_h][idx_w] = bomb

    for row in S:
        for cell in row:
            print(cell, end="")
        print()

main()
