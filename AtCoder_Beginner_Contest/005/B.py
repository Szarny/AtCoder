def main():
    most_new = 999

    N = int(input())

    for _ in range(N):
        most_new = min(
            int(input()),
            most_new
        )

    print(most_new)

main()
