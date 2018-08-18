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
    names = {
        id(v): k
        for k, v in inspect.currentframe().f_back.f_locals.items()
    }
    print(', '.join(
        names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args))


# Binary converter
def to_bin(x):
    return bin(x)[2:]


def li_input():
    return [int(_) for _ in input().split()]


# --------------------------------------------

dp = None

ans = []


def f_positive(N, A):
    global ans

    for i in range(len(A) - 1):
        ans.append((i, i + 1))


def f_negative(N, A):
    global ans

    for i in range(len(A) - 1, 0, -1):
        ans.append((i, i - 1))


def main():
    global ans

    N = int(input())
    A = li_input()

    if min(A) >= 0:
        f_positive(N, A)
    else:
        # 全てを正の整数にする
        if abs(max(A)) >= abs(min(A)):
            maxi = A.index(max(A))
            maxv = max(A)

            for i in range(len(A)):
                A[i] += maxv
                ans.append((maxi, i))

            f_positive(N, A)
        else:
            mini = A.index(min(A))
            minv = min(A)

            for i in range(len(A)):
                A[i] += minv
                ans.append((mini, i))

            f_negative(N, A)

    print(len(ans))
    for a in ans:
        print(a[0] + 1, a[1] + 1)


main()
