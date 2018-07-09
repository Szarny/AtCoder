def main():
    # (a, b) st a,b <= N and a % b >= K
    N, K = [int(i) for i in input().split()]

    ans = 0

    for a in range(N + 1):
        if a <= K:
            continue



main()
