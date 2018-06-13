def main():
    N, A, B = [int(_) for _ in input().split()]

    ans = 0

    for num in range(1, N + 1):
        if A <= sum(map(int, list(str(num)))) <= B:
            ans += num

    print(ans)

main()
