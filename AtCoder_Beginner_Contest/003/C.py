def main():
    N, K = [int(_) for _ in input().split()]
    R    = [int(_) for _ in input().split()]

    watch_list = []

    for _ in range(K):
        watch_list.append(max(R))
        R.remove(max(R))

    rate = 0
    watch_list.sort()
    for watch in watch_list:
        rate = (rate + watch) / 2

    print(rate)

main()
