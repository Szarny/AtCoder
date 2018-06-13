R = 0
C = 0
D = 0
L = 0

def fact(k):
    result = 1
    for i in range(1, k+1):
        result *= i
    return result

def ncr(n, r):
    return fact(n) // fact(r) // fact(n-r)

def c(X, Y):
    if X < 0 or Y < 0:
        return 0
    else:
        return ncr(X * Y, D) * ncr(X * Y - D, L)

def main():
    global R, C, D, L

    R, C = [int(_) for _ in input().split()]
    X, Y = [int(_) for _ in input().split()]
    D, L = [int(_) for _ in input().split()]

    result = c(X, Y)
    result -= (c((X - 1), Y) + c(X, (Y - 1))) * 2
    result += c((X - 2), Y) + c(X, (Y - 2)) + (c((X - 1), (Y - 1)) * 4)
    result -= (c((X - 2), (Y - 1)) + c((X - 1), (Y - 2))) * 2
    result += c((X - 2), (Y - 2))
    result *= (R - X + 1) * (C - Y + 1)

    print(result % 1000000007)

main()
