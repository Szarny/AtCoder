
def main():
    N, Y = map(int, input().split())

    # 最低限必要な諭吉を計算
    if 5000 * N < Y:
        n_yukichi = 1
        while True:
            if n_yukichi * 10000 + (N - n_yukichi) * 5000 >= Y:
                yukichi_need = n_yukichi
                break
            n_yukichi += 1
    else:
        yukichi_need = 0

    # 1000円の開始枚数を計算
    noguchi_start = (Y % 5000) // 1000

    for yukichi in range(yukichi_need, N+1):
        for higuchi in range(N+1):
            if yukichi + higuchi > N:
                break

            noguchi = N - yukichi - higuchi

            if yukichi + higuchi + noguchi == N:
                if yukichi*10000 + higuchi*5000 + noguchi*1000 == Y:
                    print(yukichi, higuchi, noguchi)
                    return

    print(-1, -1, -1)
    return

main()
