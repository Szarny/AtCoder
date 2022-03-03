import array
import collections
import inspect
import itertools
import math
import sys

# Set max recursion limit
sys.setrecursionlimit(1000000)


# Debug output
def chkprint(*args):
    names = {id(v): k for k, v in inspect.currentframe().f_back.f_locals.items()}
    print(", ".join(names.get(id(arg), "???") + " = " + repr(arg) for arg in args))


def to_bin(x):
    return bin(x)[2:]


def intlist_input():
    return [int(_) for _ in sys.stdin.readline().split()]


def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def gcd_list(L):
    v = L[0]

    for i in range(1, len(L)):
        v = gcd(v, L[i])

    return v


def lcm(n, m):
    return (n * m) // gcd(n, m)


def lcm_list(L):
    v = L[0]

    for i in range(1, len(L)):
        v = lcm(v, L[i])

    return v


def comb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def bisearch(L, target):
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = L[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
    if guess != target:
        return False


# --------------------------------------------

dp = None


def main():
    pass


main()
