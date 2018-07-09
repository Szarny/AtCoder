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

def calc_magic(src_y, src_x, dst_y, dst_x):
    return abs(dst_x - src_x) + abs(dst_y - src_y)

def main():
    H, W, D=list(map(int, input().split()))

    A = [[]]
    for h in range(H):
        A.append([None] + list(map(int, input().split())))

    Q = int(input())

    search_dict = {}
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            search_dict[A[y][x]] = str(y)+"-"+str(x)

    for i in range(Q):
        L, R=list(map(int, input().split()))

        tmp = search_dict[L]
        tmp = tmp.split("-")
        loc_dict = {
            "y": int(tmp[0]),
            "x": int(tmp[1])
        }

        magic = 0

        while A[loc_dict["y"]][loc_dict["x"]] != R:
            L += D

            tmp = search_dict[L]
            tmp = tmp.split("-")
            new_loc_dict = {
                "y": int(tmp[0]),
                "x": int(tmp[1])
            }

            magic += calc_magic(loc_dict["y"], loc_dict["x"], new_loc_dict["y"], new_loc_dict["x"])
            loc_dict = new_loc_dict

        print(magic)


main()
