def main():
    a = [0, 0, 0, 1]

    n = int(input())

    if n <= 3:
        print(a[n])
        return

    for i in range(4, n+1):
        a.append(sum(a[i-3:i]) % 10007)

    print(a[-1])

main()
