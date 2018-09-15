import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(1000000)


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


# Width First Search (+ Distance)
def wfs_d(D, N, K):
    """
    D: 隣接行列(距離付き)
    N: ノード数
    K: 始点ノード
    """

    dfk = [-1] * (N + 1)
    dfk[K] = 0

    cps = [(K, 0)]
    r = [False] * (N + 1)
    r[K] = True
    while len(cps) != 0:
        n_cps = []
        for cp, cd in cps:
            for i, dfcp in enumerate(D[cp]):
                if dfcp != -1 and not r[i]:
                    dfk[i] = cd + dfcp
                    n_cps.append((i, cd + dfcp))
                    r[i] = True

        cps = n_cps[:]

    return dfk


# Depth First Search (+Distance)
def dfs_d(v, pre, dist):
    """
    v:  現在のノード
    pre: １つ前のノード
    dist: 現在の距離

    以下は別途用意する
    D: 隣接リスト(行列ではない)
    D_dfs_d: dfs_d関数で用いる，始点ノードから見た距離リスト
    """

    global D
    global D_dfs_d

    D_dfs_d[v] = dist

    for next_v, d in D[v]:
        if next_v != pre:
            dfs_d(next_v, v, dist + d)

    return


def sigma(N):
    ans = 0
    for i in range(1, N + 1):
        ans += i
    return ans


def comb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

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


# --------------------------------------------

dp = None

def bisearch(L, target):
    low = 0
    high = len(L) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = L[mid]
        if guess == target:
            return True
        elif guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
    if guess != target:
        return False

def main():
    N, M = li_input()
    S = "X" + input()
    V = [i for i in range(1, N+1)]
    E = [li_input() for _ in range(M)]
    R = [False for _ in range(N+1)]

    D = collections.defaultdict(lambda: [])

    for e in E:
        D[e[0]].append(e[1])
        D[e[1]].append(e[0])

    for k in D.keys():
        D[k].sort()

    clusters = []

    for v in V:
        # 到達済みならスルー
        if R[v]:
            continue

        # 到達済みにする
        R[v] = True

        cluster = [v]
        next_v_list = D[v]

        # 幅優先探索
        while len(next_v_list) != 0:
            for next_v in next_v_list:
                new_next_v_list = []

                # 到達済みならスルー
                if R[next_v]:
                    continue

                # 到達済みにする
                R[next_v] = True

                # クラスタに加える
                cluster.append(next_v)

                new_next_v_list.extend(D[next_v])
            
            next_v_list = new_next_v_list

        clusters.append(cluster)

    # print(clusters)

    # Vectorが1なら絶対ダメなので削除
    clusters_multiple = []
    for cluster in clusters:
        if len(cluster) != 1:
            clusters_multiple.append(cluster)

    # print(clusters_multiple)

    clusters_AB = []
    # クラスタ内にAB両方が含まれていなければダメなので削除
    for cluster in clusters_multiple:
        cluster_AB = []

        for vector in cluster:
            cluster_AB.append(S[vector])

        if len(set(cluster_AB)) == 2:
            clusters_AB.append(cluster)
        
    # 要素数順にソート
    clusters_AB.sort(key=lambda l:len(l))
    
    # print(clusters_AB)

    for cluster in clusters_AB:
        # クラスタに属するVが2なら
        # 各々の自己参照と2つをつなぐEがいる
        if len(cluster) == 2:
            loop1 = bisearch(D[cluster[0]], cluster[0])
            loop2 = bisearch(D[cluster[1]], cluster[1])
            connect = bisearch(D[cluster[1]], cluster[0])

            if loop1 and loop2 and connect:
                print("Yes")
                return

        # クラスタに属するVが3なら
        # 任意の2つのVの組み合わせにおいて
        # 各々の自己参照と2つをつなぐEとABがいる
        elif len(cluster) == 3:
            for i in range(2):
                for j in range(i + 1, 3):
                    loop1 = bisearch(D[cluster[i]], cluster[i])
                    loop2 = bisearch(D[cluster[j]], cluster[j])
                    connect = bisearch(D[cluster[i]], cluster[j])
                    containAB = S[cluster[i]] != S[cluster[j]]

                    if loop1 and loop2 and connect and containAB:
                        print("Yes")
                        return

        # クラスタに属するVが4以上なら
        else:
            cluster_A = []
            cluster_B = []
            for vector in cluster:
                if S[vector] == "A":
                    cluster_A.append(vector)
                else:
                    cluster_B.append(vector)

            # print(cluster_A, cluster_B)

            # まず，ABとなる任意の2つのVの組み合わせにおいて，
            # 各々の自己参照と2つをつなぐEがいる
            for ia in range(len(cluster_A)):
                for ib in range(len(cluster_B)):
                    loop1 = bisearch(D[cluster_A[ia]], cluster_A[ia])
                    loop2 = bisearch(D[cluster_B[ib]], cluster_B[ib])
                    connect = bisearch(D[cluster_B[ib]], cluster_A[ia])

                    if loop1 and loop2 and connect:
                        print("Yes")
                        return

            # 次に，AABBとなる任意の4つのVの組み合わせにおいて
            # A - B
            # |   |
            # A - B
            # となる部分グラフがあれば成立
            for ia in range(len(cluster_A) - 1):
                for ja in range(ia + 1, len(cluster_A)):
                    for ib in range(len(cluster_B) - 1):
                        for jb in range(ib + 1, len(cluster_B)):
                            connect_aa = bisearch(D[cluster_A[ja]], cluster_A[ia])
                            connect_bb = bisearch(D[cluster_B[jb]], cluster_B[ib])
                            connect_ab1 = bisearch(D[cluster_B[ib]], cluster_A[ia]) and bisearch(D[cluster_B[jb]], cluster_A[ja])
                            connect_ab2 = bisearch(D[cluster_B[jb]], cluster_A[ia]) and bisearch(D[cluster_B[ib]], cluster_A[ja])

                            if connect_aa and connect_bb and (connect_ab1 or connect_ab2):
                                print("Yes")
                                return
    
    print("No")



                


main()
