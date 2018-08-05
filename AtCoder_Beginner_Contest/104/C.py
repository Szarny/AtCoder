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
    names = {id(v): k for k, v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))

# Binary converter


def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]

# --------------------------------------------


dp = None


def main():
    D, G = li_input()
    Questions = []
    Points = []
    S = [[], [], []]

    for i in range(1, D+1):
        Questions.append(li_input())
        Points.append(i * 100)

    for i in range(D):
        S[0].append(Points[i] * (Questions[i][0] - 1))
        S[1].append(Points[i] * Questions[i][0] + Questions[i][1])

    t = 0
    while True:
        for i in range(D)


main()
