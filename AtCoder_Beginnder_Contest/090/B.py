def f(k):
    k = str(k)

    for i in range(len(k) // 2):
        if k[i] != k[len(k) - i - 1]:
            return False

    return True

def main():
    A, B = [int(i) for i in input().split()]

    ans = 0
    for k in range(A, B + 1):
        if f(k):
            ans += 1

    print(ans)

main()
