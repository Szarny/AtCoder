import itertools

def fact(k):
    result = 1
    for i in range(1, k+1):
        result *= i
    return result

def main():
    R, C = [int(_) for _ in input().split()]
    X, Y = [int(_) for _ in input().split()]
    D, L = [int(_) for _ in input().split()]

    # 面積を求める
    area_all = R * C
    area_section = X * Y

    # 指定区画の中で空っぽの領域数を計算する
    E = area_section - (D + L)

    # 長方形の取り方のパターンを調べる
    v_diff = R - X
    h_diff = C - Y
    pattern = (v_diff + 1) * (h_diff + 1)

    result = (fact(E + D + L) // (fact(E) * fact(D) * fact(L))) * pattern

    print(result % 1000000007)

main()
