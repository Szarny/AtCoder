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
    name_list = [input() for i in range(N)]
    first_letter_dict = collections.defaultdict(lambda: 0)

    for name in name_list:
        first_letter_dict[name[0]] += 1

    first_letter_combination = [
        "MAR", "MAC", "MAH", "MRC", "MRH", "MCH", "ARC", "ARH", "ACH", "RCH"
    ]

    combinations = 0

    for f_comb in first_letter_combination:
        combinations += first_letter_dict[f_comb[0]] * first_letter_dict[f_comb[1]] * first_letter_dict[f_comb[2]]

    print(combinations)


main()
