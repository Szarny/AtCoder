import itertools

def fact(k):
    result = 1
    for i in range(1, k+1):
        result *= i
    return result

def main():
    V_src, H_src = [int(_) for _ in input().split()]
    V_dst, H_dst = [int(_) for _ in input().split()]
    Desk, Lac    = [int(_) for _ in input().split()]

    # 面積を求める
    Area_src = V_src * H_src
    Area_dst = V_dst * H_dst

    # 空っぽの領域数を計算する
    Empty = Area_dst - (Desk + Lac)

    # 長方形の取り方のパターンを調べる
    V_diff = V_src - V_dst
    H_diff = H_src - H_dst
    pattern = (V_diff + 1) * (H_diff + 1)

    result = (fact(Empty + Desk + Lac) // (fact(Empty) * fact(Desk) * fact(Lac))) * pattern

    print(result % 1000000007)

main()
