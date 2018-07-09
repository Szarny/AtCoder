import sys
import math
import collections
import itertools
import array
import inspect
import pprint

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

def main():
    delta_x = [-1, 0, 0, 1]
    delta_y = [0, -1, 1, 0]

    H, W = list(map(int, input().split()))

    S = []
    for _ in range(H):
        S.append(list(input()))

    S[0][0] = 0

    reached = [[0, 0]]
    move = 1

    while len(reached) != 0:
        new_reached = []

        for r in reached:
            for dx, dy in zip(delta_x, delta_y):
                new_y = r[0] + dy
                new_x = r[1] + dx

                if not (0 <= new_y < H):
                    continue

                if not(0 <= new_x < W):
                    continue

                if S[new_y][new_x] == ".":
                    S[new_y][new_x] = move
                    new_reached.append([new_y, new_x])

        move += 1
        reached = new_reached

    if S[-1][-1] == "." or S[-1][-1] == "#":
        print(-1)
        return


    i = H-1
    j = W-1
    while True:
        current = S[i][j]

        if current == 0:
            break
        S[i][j] = "#"


        for dx, dy in zip(delta_x, delta_y):
            new_y = i + dy
            new_x = j + dx

            if not (0 <= new_y < H):
                continue

            if not(0 <= new_x < W):
                continue

            if S[new_y][new_x] == current - 1:
                i = new_y
                j = new_x
                break

    S[0][0] = "#"

    point = 0
    for row in S:
        for cell in row:
            if isinstance(cell, int) or cell == ".":
                point += 1

    print(point)





main()
