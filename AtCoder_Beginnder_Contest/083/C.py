def main():
    lower, upper = list(map(int, input().split()))

    n_gift = 1

    current_num = lower * 2

    while current_num <= upper:
        current_num *= 2
        n_gift += 1

    print(n_gift)

main()
