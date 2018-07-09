def main():
    N, M = list(map(int, input().split()))

    for adult in range(N+1):
        for old in range(N-adult+1):
            child = N - adult - old

            if 2*adult + 3*old + 4*child == M:
                print(adult, old, child)
                return

    print(-1, -1, -1)

main()
