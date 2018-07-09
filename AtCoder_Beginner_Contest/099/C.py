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
    N = int(input())

    draws = [1]

    for beki in range(99999):
        over = 0

        if 6 ** beki > 100000:
            over += 1
        else:
            draws.append(6 ** beki)

        if 9 ** beki > 100000:
            over += 1
        else:
            draws.append(9 ** beki)

        if over == 2:
            break

    draws.sort(reverse=True)

    ans = 0
    idx = 0
    while N != 0:
        if draws[idx] > N:
            idx += 1
            continue
        if 12 <= N <= 14:
            N -= 6
            ans += 1
        else:
            N -= draws[idx]
            ans += 1

    print(ans)

main()
