def calc_sum_of_digit(k):
    _sum = 0

    for i in k:
        _sum += int(i)

    return _sum

def main():
    N, A, B = list(map(int, input().split()))

    result = 0
    for i in range(1, N+1):
        sum_of_digit = calc_sum_of_digit(str(i))

        if A <= sum_of_digit <= B:
            result += i

    print(result)


main()
