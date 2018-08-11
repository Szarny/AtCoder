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
c = []


# (i < limit, c[i] > 0となるc[i]の数を足して行った結果) + 現在の値 が
# Nを下回ればc[limit]を足す必要がある
def is_lower(limit, c_value, N):
    add_value = 0
    for i in range(limit - 1, -1, -1):
        if c[i] > 0:
            add_value += c[i]

    return c_value + add_value < N


# (i < limit c[i] < 0となるc[idx]の数の総和) + 現在の値 が
# Nを上回ればc[limit]を引く必要がある
def is_over(limit, c_value, N):
    sub_value = 0
    for i in range(limit - 1, -1, -1):
        if c[i] < 0:
            sub_value += c[i]

    return c_value + sub_value > N


def main():
    global c

    N = int(input())
    c_value = None

    # コーナーケース
    if N == 0:
        print(0)
        return

    # 位を事前に計算
    for i in range(50):
        c.append((-2)**i)

    # NがPositiveの場合
    # (-2)**i (i=2k) の総和が目的の値を超えるところが最上位ビット
    if N > 0:
        tmpsum = 0
        for i in range(50):

            if c[i] > 0:
                tmpsum += c[i]

            if tmpsum >= N:
                idx = i
                c_value = c[i]
                break

    # NがNegativeの場合
    # (-2)**i (i=2k+1) の総和が目的の値を下回るところが最上位ビット
    else:
        tmpsub = 0
        for i in range(50):
            if c[i] < 0:
                tmpsub += c[i]

            if tmpsub <= N:
                idx = i
                c_value = c[i]
                break

    ans = "1"

    for c_idx in range(idx - 1, -1, -1):
        # c[c_idx]がNegativeのとき
        # c[c_idx]の値を加算しなければ
        # c_idx' < c_idx かつ c[c_idx']<0 となる任意のc[c_idx']の値を加算しても
        # 最終的な総和がNを上回ってしまうなら，c[c_idx]を加算する必要がある
        if c[c_idx] < 0:
            if is_over(c_idx, c_value, N):
                ans += "1"
                c_value += c[c_idx]
            else:
                ans += "0"

        # c[c_idx]がPositiveのとき
        # c[c_idx]の値を加算しなければ
        # c_idx' < c_idx かつ c[c_idx']>0 となる任意のc[c_idx']の値を加算しても
        # 最終的な総和がNを下回ってしまうなら，c[c_idx]を加算する必要がある
        else:
            if is_lower(c_idx, c_value, N):
                ans += "1"
                c_value += c[c_idx]
            else:
                ans += "0"

    print(ans)


main()
