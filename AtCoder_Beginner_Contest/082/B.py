def main():
    S = "".join(sorted(list(input())))
    T = "".join(sorted(list(input()), reverse=True))

    if S < T:
        print("Yes")
    else:
        print("No")

main()
