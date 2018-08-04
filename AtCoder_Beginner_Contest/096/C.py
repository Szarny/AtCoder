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
    H, W = map(int, input().split())
    S = []
    Dx, Dy = [-1, 0, 0, 1], [0, -1, 1, 0]

    for i in range(H):
        S.append(input())

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                flg = False
                for dx, dy in zip(Dx, Dy):
                    x = i + dx
                    y = j + dy

                    if not (0 <= x < H and 0 <= y < W):
                        continue

                    if S[x][y] == "#":
                        flg = True
                        break
                
                if not flg:
                    print("No")
                    sys.exit()
    
    print("Yes")


main()
