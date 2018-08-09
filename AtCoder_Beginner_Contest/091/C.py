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


def is_inside_and_short(r, b, minb):
    c1 = r[0] < b[0] and r[1] < b[1]
    c2 = math.sqrt((b[0]**2) +
                   (b[1]**2)) < math.sqrt((minb[0]**2) + minb[1]**2)

    return c1 and c2


def is_inside_and_minx(r, b, minb):
    c1 = r[0] < b[0] and r[1] < b[1]
    c2 = b[0] < minb[0]

    return c1 and c2


def is_inside_and_miny(r, b, minb):
    c1 = r[0] < b[0] and r[1] < b[1]
    c2 = b[1] < minb[1]

    return c1 and c2


def is_inside_and_minxy(r, b, minb):
    c1 = r[0] < b[0] and r[1] < b[1]
    c2 = b[0] < minb[0] and b[1] < minb[1]

    return c1 and c2


def count(R, B, is_func):
    ans = 0
    Btmp = [x[:] for x in B]

    for r in R:
        minb = [999, 999]
        is_find = False

        for b in Btmp:
            if is_func(r, b, minb):
                minb = b
                is_find = True

        if is_find:
            ans += 1
            Btmp.remove(minb)

    return ans


def main():
    N = int(input())
    R = [li_input() for _ in range(N)]
    B = [li_input() for _ in range(N)]

    maxpair = 0

    # Rを原点からの距離順に並べ替える
    Rsort_dist = sorted(R, key=lambda r: math.sqrt((r[0]**2) + (r[1]**2)))

    # Rをx座標順に並べ替える
    Rsort_x = sorted(R, key=lambda r: r[0])

    # Rをy座標順に並べ替える
    Rsort_y = sorted(R, key=lambda r: r[1])

    for is_func in [
            is_inside_and_short, is_inside_and_minx, is_inside_and_miny,
            is_inside_and_minxy
    ]:
        maxpair = max(
            count(Rsort_dist, B, is_func),
            count(Rsort_x, B, is_func),
            count(Rsort_y, B, is_func),
        )

    print(maxpair)


main()
