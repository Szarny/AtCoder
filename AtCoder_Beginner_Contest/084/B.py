def main():
    A, B = list(map(int, input().split()))
    S = input()

    for idx in range(len(S)):
        if idx == A:
            if S[idx] != "-":
                print("No")
                return

        else:
            if not S[idx].isdigit():
                print("No")
                return

    print("Yes")

main()
