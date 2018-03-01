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
    Sp = input()
    T = input()

    is_restorable = False
    replace_start_idx = None
    replace_end_idx = None

    for start_idx in range(len(Sp) - len(T) + 1):
        target_idx = 0
        while target_idx < len(T):
            if T[target_idx] == Sp[start_idx + target_idx] or Sp[start_idx + target_idx] == "?":
                target_idx += 1

                if target_idx == len(T):
                    is_restorable = True
                    replace_start_idx = start_idx
                    replace_end_idx = start_idx + target_idx
            else:
                break

    if not is_restorable:
        print("UNRESTORABLE")
    else:
        idx = 0
        while idx < len(Sp):
            if replace_start_idx <= idx < replace_end_idx:
                for t in T:
                    print(t, end="")
                idx += len(T)
            elif Sp[idx] == "?":
                print("a", end="")
                idx += 1
            else:
                print(Sp[idx], end="")
                idx += 1


main()
