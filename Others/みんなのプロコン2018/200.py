def main():
    X, K = [int(_) for _ in input().split()]
    X_store = X

    X += 10**K
    X_r = X % 10**K

    print(X - X_r)

main()
